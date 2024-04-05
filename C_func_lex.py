import ply.lex as lex

#define TOKENS
tokens = ('DTYPE',
          'ID',
          'OP',
          'LBRACE',
          'RBRACE',
          'COMMA',
          'SEMICOLON',
          'LFLOWER',
          'RFLOWER')


def t_DTYPE(t): 
    r'\b(int|void|char|double|bool|float)\b'
    return t

def t_ID(t):
    r'\b[a-zA-Z_][a-zA-Z0-9_]*\b' 
    return t


t_LBRACE = r'\('
t_RBRACE = r'\)'

def t_COMMA(t):
    r','
    return t

def t_SEMICOLON(t):
    r';'
    return t

def t_LFLOWER(t):
    r'{'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_RFLOWER(t):
    r'}'
    return t


t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character encountered {t.value[0]}")
    t.lexer.skip(1)
    
lexer = lex.lex()

data = input()

lexer.input(data)

while(1):
     tok = lexer.token()
     if not tok:
         break
     print(tok)