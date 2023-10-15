import ply.lex as lex

literals = ['+', '-', '*', '/',
            '{', '}', '[', ']', '(', ')',
            '=', ',', ';', ':', "'", ]

tokens = [
    'FOR', 'WHILE', 'IF', 'ELSE', 'RETURN', 'BREAK', 'CONTINUE', 'PRINT',
    'DOTADD', 'DOTSUB', 'DOTMUL', 'DOTDIV', 'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN',
    'EQ', 'NE', 'GE', 'LE', 'GT', 'LT', 'EYE', 'ZEROS', 'ONES',
    'ID', 'STRING', 'INTNUM', 'FLOAT',
]

keywords = {
    'for': 'FOR',
    'while': 'WHILE',
    'if': 'IF',
    'else': 'ELSE',
    'return': 'RETURN',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'print': 'PRINT',
    'eye': 'EYE',
    'zeros': 'ZEROS',
    'ones': 'ONES',
}

parsing_errors = []


t_FOR = r'for'
t_WHILE = r'while'
t_IF = r'if'
t_ELSE = r'else'
t_RETURN = r'return'
t_BREAK = r'break'
t_CONTINUE = r'continue'
t_PRINT = r'print'
t_DOTADD = r'\.\+'
t_DOTSUB = r'\.-'
t_DOTMUL = r'\.\*'
t_DOTDIV = r'\./'
t_ADDASSIGN = r'\+='
t_SUBASSIGN = r'-='
t_MULASSIGN = r'\*='
t_DIVASSIGN = r'/='
t_EQ = r'=='
t_NE = r'!='
t_GE = r'>='
t_LE = r'<='
t_GT = r'>'
t_LT = r'<'
t_EYE = r'eye'
t_ZEROS = r'zeros'
t_ONES = r'ones'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = keywords.get(t.value, 'ID')
    return t


def t_FLOAT(t):
    r'\d*\.\d+|\d+\.\d*'
    t.value = float(t.value)
    return t


def t_INTNUM(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    return t


t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_COMMENT(t):
    r'\#.*'
    pass


def t_error(t):
    msg = f'Parse error at line {t.lineno}. Unexpected character: {t.value[0]}'
    parsing_errors.append(msg)
    print(msg)
    t.lexer.skip(1)


def lex_init():
    return lex.lex()
