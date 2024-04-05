import ply.yacc as yacc
from c_for_lex import tokens

flag = 0

def p_for(p):
    '''
    for_statement     : FOR LBRACE conditions RBRACE LFLOWER statements RFLOWER
                        | FOR LBRACE conditions RBRACE singleStatement 
    '''
    if len(p) == 6:
        p[0] = (p[1],p[3],p[5])
    else:
        p[0] = (p[1],p[3],p[6])

def p_statements(p):
    '''
    statements  : statements statement
                | statement
    '''
    if len(p) == 2:
        p[0] = (p[1],)
    else:
        p[0] = p[1]+(p[2],)

def p_statement(p):
    '''
    statement   : list SEMICOLON
                | for_statement
                | empty
    '''
    if len(p) == 3:
        p[0] = (p[1],)
    else:
        p[0] = p[1]

def p_singleStatement(p):
    '''
    singleStatement  : list SEMICOLON 
                    | empty
                    | for_statement
    '''
    if len(p) == 3:
        p[0] = (p[1],)
    else:
        p[0] = p[1]

def p_list(p):
    '''
    list    : ID list
            | ID
    '''

    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]]+p[2]

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

def p_conditions(p):
    '''
    conditions  : DTYPE ID EQUALS ID SEMICOLON ID GREATER ID SEMICOLON ID PLUS PLUS
                | DTYPE ID EQUALS ID SEMICOLON ID LESSER ID SEMICOLON ID PLUS PLUS
                | DTYPE ID EQUALS ID SEMICOLON ID GREATER EQUALS ID SEMICOLON ID PLUS PLUS
                | DTYPE ID EQUALS ID SEMICOLON ID LESSER EQUALS ID SEMICOLON ID PLUS PLUS
                | DTYPE ID EQUALS ID SEMICOLON ID NOT EQUALS ID SEMICOLON ID PLUS PLUS
                | DTYPE ID EQUALS ID SEMICOLON ID GREATER ID SEMICOLON ID MINUS MINUS
                | DTYPE ID EQUALS ID SEMICOLON ID LESSER ID SEMICOLON ID MINUS MINUS
                | DTYPE ID EQUALS ID SEMICOLON ID GREATER EQUALS ID SEMICOLON ID MINUS MINUS
                | DTYPE ID EQUALS ID SEMICOLON ID LESSER EQUALS ID SEMICOLON ID MINUS MINUS
                | DTYPE ID EQUALS ID SEMICOLON ID NOT EQUALS ID SEMICOLON ID MINUS MINUS
    '''

    if len(p) == 2:
        p[0] = ('condition',p[1])
    else :
        p[0] = ('condition',p[1],p[2],p[3])

def p_error(p):
    print("Syntax error")
    global flag 
    flag = 1


#From here, just copy paste and change the input statement for every other construct
#Don't forget to globally declare flag and also make flag 1 at error 
parser = yacc.yacc()
while True:
   flag = 0
   try:
       s = input('enter the conditional statement:')
   except EOFError:
       break
   if not s: 
            flag = 0
            continue
   result = parser.parse(s)
   if flag == 0:
        print("Valid syntax")
        print("Result:", result)
