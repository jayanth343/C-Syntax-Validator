
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'IDENTIFIER LBRACE LPAREN RBRACE RPAREN SEMICOLON WHILEwhile_loop : WHILE LPAREN condition RPAREN LBRACE statements RBRACEcondition : IDENTIFIERstatements : statement statements\n                  | statementstatement : while_loop\n                 | condition SEMICOLON'
    
_lr_action_items = {'WHILE':([0,7,10,11,12,13,],[2,2,2,-5,-6,-1,]),'$end':([1,13,],[0,-1,]),'LPAREN':([2,],[3,]),'IDENTIFIER':([3,7,10,11,12,13,],[5,5,5,-5,-6,-1,]),'RPAREN':([4,5,],[6,-2,]),'SEMICOLON':([5,8,],[-2,12,]),'LBRACE':([6,],[7,]),'RBRACE':([9,10,11,12,13,14,],[13,-4,-5,-6,-1,-3,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'while_loop':([0,7,10,],[1,11,11,]),'condition':([3,7,10,],[4,8,8,]),'statements':([7,10,],[9,14,]),'statement':([7,10,],[10,10,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> while_loop","S'",1,None,None,None),
  ('while_loop -> WHILE LPAREN condition RPAREN LBRACE statements RBRACE','while_loop',7,'p_while_loop','C_wh.py',43),
  ('condition -> IDENTIFIER','condition',1,'p_condition','C_wh.py',47),
  ('statements -> statement statements','statements',2,'p_statements','C_wh.py',51),
  ('statements -> statement','statements',1,'p_statements','C_wh.py',52),
  ('statement -> while_loop','statement',1,'p_statement','C_wh.py',59),
  ('statement -> condition SEMICOLON','statement',2,'p_statement','C_wh.py',60),
]
