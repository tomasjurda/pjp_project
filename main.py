from antlr4 import *
from ProjectLexer import ProjectLexer
from ProjectParser import ProjectParser
from ProjectParserListener import ProjectParserListener


def main():
    source_code = """
    write "<Constants>";
    write "10: ",10;
    write " 1.25: ", 1.25;
    write "";;

    write "<Variables>";
    string s;
    s="Abcd";
    write "s(Abcd): ", s;

    float d;
    d=3.141592;
    write "d(3.141592): ", d;

    int n;
    n=-500;
    write "n(-500): ", n;
    write "";
    
    bool boolean;
    boolean=true;
    write "boolean(true): ",boolean;
    write "";

    write "<Expressions>";
    write "2+3*5(17): ",2+3*5;
    write "17 / 3(5): ", 17 / 3;
    write "17 % 3(2): ", 17 % 3;
    write "2.5*2.5/6.25(1.0): ", 2.5*2.5/6.25;
    write "1.5*3(4.5): ", 1.5*3;
    write "abc+def (abcdef): ", "abc"."def";
    write "";
    """

    input_stream = InputStream(source_code)
    lexer = ProjectLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = ProjectParser(tokens)

    tree = parser.program()

    listener = ProjectParserListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)


if __name__ == "__main__":
    main()
