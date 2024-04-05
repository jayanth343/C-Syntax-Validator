import ply.lex as lex

tokens = ('FOR',
        'LBRACE',
        'DTYPE',
        'LESSER',
        'GREATER',
        'NOT',
        'AND',
        'OR',
        'OP',
        'COMMA',
        'EQUALS',
        'RBRACE',
        'LFLOWER',
        'RFLOWER',
        'SEMICOLON',
        'ID',
        'PLUS',
        'MINUS')

def t_FOR(t):
    r'for'
    return t

t_LBRACE = r'\('
t_RBRACE = r'\)'
t_LFLOWER = r'\{'
t_RFLOWER = r'\}'
t_PLUS    = r'\+'
t_MINUS   = r'-'
def t_DTYPE(t): 
    r'\b(int|void|char|double|bool|float)\b'
    return t


def t_ID(t):
    r'\b([a-zA-Z_][a-zA-Z_0-9]*)\b |\b(\d+)\b'
    return t

t_OP = r'\+\-'
t_COMMA = r','
t_LESSER = r'<'
t_GREATER = r'>'
t_EQUALS = r'=(=)?'
t_NOT = r'!'
t_AND = r'&&'
t_OR = r'\|\|'
t_SEMICOLON = r';'

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character found {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

data = input()

lexer.input(data)

while(1):
    tok = lexer.token()
    if not tok:
        break
    print(tok)  