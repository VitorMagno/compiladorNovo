# Generated from BigT.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\3\2\2\2\5\3\3\2\2\2\2")
        return buf.getvalue()


class BigTParser ( Parser ):

    grammarFileName = "BigT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'IF'", "'ELSE'", "'WHILE'", "'&&'", "'||'", 
                     "'!'", "'>='", "'<='", "'=='", "'<'", "'>'", "'*'", 
                     "'/'", "'+'", "'-'", "<INVALID>", "<INVALID>", "'SEQ'", 
                     "'PAR'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "WHILE", "AND", "OR", "NOT", 
                      "GE", "LE", "EQ", "LT", "GT", "MUL", "DIV", "ADD", 
                      "SUB", "ID", "NEWLINE", "SEQ", "PAR", "INT", "WS" ]

    RULE_programa_minipar = 0

    ruleNames =  [ "programa_minipar" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    WHILE=3
    AND=4
    OR=5
    NOT=6
    GE=7
    LE=8
    EQ=9
    LT=10
    GT=11
    MUL=12
    DIV=13
    ADD=14
    SUB=15
    ID=16
    NEWLINE=17
    SEQ=18
    PAR=19
    INT=20
    WS=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Programa_miniparContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BigTParser.RULE_programa_minipar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma_minipar" ):
                listener.enterPrograma_minipar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma_minipar" ):
                listener.exitPrograma_minipar(self)




    def programa_minipar(self):

        localctx = BigTParser.Programa_miniparContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa_minipar)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





