import ply
import sys
import ply.lex as lex


tokens = ('PLUS',  'MINUS',  'TIMES',  'DIVIDE',
          'LPAREN',  'RPAREN',  'NUMBER', 'ID')

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

literals = ['+', '-', '*', '/', '(', ')']


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z_]\w*'
    return t


t_ignore = '  \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()
fh = open(sys.argv[1], "r")
lexer.input(fh.read())
for token in lexer:
    print(f"line {token.lineno}: {token.type}({token.value})")
