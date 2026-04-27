class SymbolTable:
    def __init__(self, errors_list):
        self._variables = {}
        self.errors = errors_list

    def declare(self, key, var_type, line):
        if key in self._variables:
            self.errors.append(
                f"Semantic Error [line {line}]: Multiple declaration of variable '{key}'"
            )
        else:
            self._variables[key] = var_type

    def resolve(self, key, line=None):
        if key not in self._variables:
            self.errors.append(
                f"Semantic Error [line {line}]: Unknown variable '{key}'"
            )
            return "error"
        else:
            return self._variables[key]

    """
    def __setitem__(self, key, value):
        if key in self._variables:
            print(f"Multiple declaration of variable '{key}'")
            return "error"
        else:
            self._variables[key] = value

    def __getitem__(self, key):
        if key not in self._variables:
            print(f"Unknown variable '{key}'")
            return "error"
        else:
            return self._variables[key]
    """

    def __str__(self):
        s = ""
        for var in self._variables:
            s += f"Variable {var} is type {self._variables[var]}\n"
        return s
