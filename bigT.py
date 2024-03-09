import sys
from antlr4 import *
from BigTLexer import BigTLexer
from BigTParser import BigTParser
from VisitorInterp import VisitorInterp

def main(argv):
    input_stream = InputStream(sys.stdin.readline())
    lexer = BigTLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = BigTParser(stream)
    tree = parser.progama_minipar()

    visitor = VisitorInterp()
    visitor.visit(tree)

if __name__ == '__main__':
    main(sys.argv)