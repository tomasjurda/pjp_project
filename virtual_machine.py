import shlex
from enum import Enum


class State(Enum):
    NORMAL = 1
    SEARCHING = 2


class VirtualMachine:

    def __init__(self, code_path):
        self.memory = {}
        self.stack = []

        self.labels = {}
        self.state = State.NORMAL
        self.searching_for = None

        self.instructions = self.load_instructions(code_path)

    def load_instructions(self, cpath):
        with open(cpath, "r") as f:
            return f.readlines()

    def run(self):
        i = 0
        num_of_instr = len(self.instructions)
        while i < num_of_instr:
            ins = self.instructions[i]

            if self.state == State.NORMAL:
                if ins.startswith("push"):
                    values = shlex.split(ins)
                    if values[1] == "I":
                        value = int(values[2])
                    elif values[1] == "F":
                        value = float(values[2])
                    elif values[1] == "B":
                        if values[2] == "true":
                            value = True
                        else:
                            value = False
                    else:
                        value = values[2]
                    self.stack.append(value)

                elif ins.startswith("pop"):
                    self.stack.pop()

                elif ins.startswith("save"):
                    values = ins.split(" ")
                    value = self.stack.pop()
                    self.memory[values[1]] = value

                elif ins.startswith("print"):
                    values = ins.split(" ")
                    n_value = int(values[1])
                    row = ""
                    for _ in range(n_value):
                        value = self.stack.pop()
                        row = str(value) + row
                    print(row)

                elif ins.startswith("load"):
                    values = ins.split(" ")
                    value = self.memory[values[1]]
                    self.stack.append(value)

                elif ins.startswith("add"):
                    value_2 = self.stack.pop()
                    value_1 = self.stack.pop()
                    self.stack.append(value_1 + value_2)

                elif ins.startswith("sub"):
                    value_2 = self.stack.pop()
                    value_1 = self.stack.pop()
                    self.stack.append(value_1 - value_2)

                elif ins.startswith("concat"):
                    value_2 = self.stack.pop()
                    value_1 = self.stack.pop()
                    self.stack.append(value_1 + value_2)

                elif ins.startswith("mod"):
                    value_2 = self.stack.pop()
                    value_1 = self.stack.pop()
                    self.stack.append(value_1 % value_2)

                elif ins.startswith("div"):
                    values = ins.split(" ")
                    value_2 = self.stack.pop()
                    value_1 = self.stack.pop()

                    if values[1] == "I":
                        self.stack.append(value_1 // value_2)
                    else:
                        self.stack.append(value_1 / value_2)

                elif ins.startswith("mul"):
                    value_2 = self.stack.pop()
                    value_1 = self.stack.pop()
                    self.stack.append(value_1 * value_2)

                elif ins.startswith("uminus"):
                    values = ins.split(" ")
                    value = self.stack.pop()

                    self.stack.append(value * (-1))

                elif ins.startswith("itof"):
                    value = self.stack.pop()
                    value = float(value)

                    self.stack.append(value)

                elif ins.startswith("read"):
                    values = ins.split(" ")
                    value = input()

                    dtype = values[1]

                    try:
                        if dtype == "I":
                            value = int(value)
                        elif dtype == "F":
                            value = float(value)
                        elif dtype == "B":
                            if value == "true":
                                value = True
                            elif value == "false":
                                value = False
                            else:
                                raise ValueError()
                    except ValueError:
                        print(
                            f"Runtime Error: Couldn't convert {value} to type {dtype}"
                        )
                        return

                    self.stack.append(value)

                elif ins.startswith("lt"):
                    value_2 = self.stack.pop()
                    value_1 = self.stack.pop()
                    self.stack.append(value_1 < value_2)

                elif ins.startswith("gt"):
                    value_2 = self.stack.pop()
                    value_1 = self.stack.pop()
                    self.stack.append(value_1 > value_2)

                elif ins.startswith("eq"):
                    value_2 = self.stack.pop()
                    value_1 = self.stack.pop()
                    self.stack.append(value_1 == value_2)

                elif ins.startswith("and"):
                    value_2 = self.stack.pop()
                    value_1 = self.stack.pop()
                    self.stack.append(value_1 and value_2)

                elif ins.startswith("or"):
                    value_2 = self.stack.pop()
                    value_1 = self.stack.pop()
                    self.stack.append(value_1 or value_2)

                elif ins.startswith("not"):
                    value = self.stack.pop()
                    self.stack.append(not value)

                elif ins.startswith("jmp"):
                    values = ins.split(" ")
                    label = values[1]
                    if label not in self.labels:
                        self.state = State.SEARCHING
                        self.searching_for = label
                    else:
                        i = self.labels[label]

                elif ins.startswith("fjmp"):
                    value = self.stack.pop()

                    if not value:
                        values = ins.split(" ")
                        label = values[1]
                        if label not in self.labels:
                            self.state = State.SEARCHING
                            self.searching_for = label
                        else:
                            i = self.labels[label]

            if ins.startswith("label"):
                values = ins.split(" ")
                label = values[1]
                if label not in self.labels:
                    self.labels[label] = i

                if self.state == State.SEARCHING:
                    if self.searching_for == label:
                        self.state = State.NORMAL
                        self.searching_for = None

            i += 1
