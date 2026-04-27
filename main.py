import sys

from antlr4 import *
from ProjectLexer import ProjectLexer
from ProjectParser import ProjectParser
from MyListener import MyListener
from MyVisitor import MyVisitor
from MyErrorListener import MyErrorListener
from virtual_machine import VirtualMachine


def main():
    source_code = """write "<Relational operators>";
    write "1<5: ", 1 < 5;
    write "1>3.5: ", 1 > 3.5;
    write "aa==aa: ", "aa"=="aa";
    write "aa==ab: ", "aa"=="ab";
    write "aa!=ab: ", "aa"!="ab";
    write "";
    write "<Logic operators>";
    write "false and true (false):", false && true;
    write "false or true (true):", false || true;
    write "not 1==2 (true):", !(1==2);
    write "true or false and true (true):", true || false && true;
    """

    input_stream = InputStream(source_code)
    lexer = ProjectLexer(input_stream)

    error_listener = MyErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)

    tokens = CommonTokenStream(lexer)
    parser = ProjectParser(tokens)

    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.program()

    if len(error_listener.errors) > 0:
        print("SYNTAX ERRORS FOUND!!")
        for err in error_listener.errors:
            print(err)
        print("Compilation stopped.")
        sys.exit(1)

    listener = MyListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    if len(listener.errors) > 0:
        print("TYPE ERRORS FOUND!!")
        for err in listener.errors:
            print(err)
        print("Compilation stopped.")
        sys.exit(1)

    # print(listener.symbol_table)

    visitor = MyVisitor(listener.symbol_table, listener.types)
    instructions = visitor.visit(tree)

    with open("instructions.txt", "w") as f:
        f.write(instructions)

    vmachine = VirtualMachine("instructions.txt")
    vmachine.run()


if __name__ == "__main__":
    main()
