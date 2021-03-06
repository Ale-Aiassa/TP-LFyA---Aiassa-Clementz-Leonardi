
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND AS ASC BY CADENA COMA COMILLA COUNT DESC DISTINCT DISTINTO FROM GROUP HAVING IGUAL IN INNER IS JOIN LEFT MAX MAYOR MAYOR_O_IGUAL MENOR MENOR_O_IGUAL MIN NOT NULL NUMERO ON OR ORDER PARENTESIS_DERECHO PARENTESIS_IZQUIERDO PUNTO SELECT WHERECONS : SELECT_ FROM_ JOIN_ WHERE_ GROUP_BY ORDER_BYSELECT_ : SELECT CAMPOS\n\t| SELECT DISTINCT CAMPOSCAMPOS : CAMPO COMA CAMPOS\n\t| CAMPOCAMPO : CADENA PUNTO CADENA\n\t| CADENA PUNTO CADENA AS COMILLA CADENA COMILLA\n\t| FUNCION AS COMILLA CADENA COMILLAFUNCION : MIN PARENTESIS_IZQUIERDO CADENA PUNTO CADENA PARENTESIS_DERECHO\n\t| MAX PARENTESIS_IZQUIERDO CADENA PUNTO CADENA PARENTESIS_DERECHO\n\t| COUNT PARENTESIS_IZQUIERDO CADENA PUNTO CADENA PARENTESIS_DERECHO\n\t| COUNT PARENTESIS_IZQUIERDO DISTINCT CADENA PUNTO CADENA PARENTESIS_DERECHOFROM_ : FROM CADENA\n\t| FROM CADENA CADENA\n\t| FROM CADENA AS CADENA JOIN_ : ELECCION_JOIN JOIN_\n\t|  ELECCION_JOIN : INNER JOIN CADENA ON CONDICION_\n\t| INNER JOIN CADENA CADENA ON CONDICION_\n\t| INNER JOIN CADENA AS CADENA ON CONDICION_\n\t| LEFT JOIN CADENA ON CONDICION_\n\t| LEFT JOIN CADENA CADENA ON CONDICION_\n\t| LEFT JOIN CADENA AS CADENA ON CONDICION_ CONDICION_ : CONDICION\n\t| CONDICION_ AND CONDICION_\n\t| CONDICION_ OR CONDICION_\n\t| PARENTESIS_IZQUIERDO CONDICION_ OR CONDICION_ PARENTESIS_DERECHO\n\t| CADENA PUNTO CADENA SUBCONS  CONDICION : CADENA PUNTO CADENA OPERADOR_COMPARATIVO VALOR\n\t| CADENA PUNTO CADENA OPERADOR_COMPARATIVO CADENA PUNTO CADENA\n\t| CADENA PUNTO CADENA NULLABLE  OPERADOR_COMPARATIVO : MENOR\n\t| IGUAL\n\t| MAYOR\n\t| MENOR_O_IGUAL\n\t| MAYOR_O_IGUAL\n\t| DISTINTO VALOR : NUMERO\n\t| COMILLA CADENA COMILLA NULLABLE : IS NULL\n\t| IS NOT NULLSUBCONS : IN PARENTESIS_IZQUIERDO CONS PARENTESIS_DERECHO\n\t| NOT IN PARENTESIS_IZQUIERDO CONS PARENTESIS_DERECHOWHERE_ : WHERE CONDICION_\n\t| GROUP_BY : GROUP BY CAMPOS_AGRUPADOS HAVING_\n\t| CAMPOS_AGRUPADOS : CADENA PUNTO CADENA COMA CAMPOS_AGRUPADOS\n\t| CADENA PUNTO CADENAHAVING_ : HAVING FUNCION OPERADOR_COMPARATIVO VALOR\n\t| ORDER_BY : ORDER BY CAMPOS_ORDENADOS\n\t| CAMPOS_ORDENADOS : CADENA PUNTO CADENA ORDEN COMA CAMPOS_ORDENADOS\n\t| CADENA PUNTO CADENA ORDENORDEN : ASC\n\t| DESC\n\t| '
    
_lr_action_items = {'SELECT':([0,124,136,],[3,3,3,]),'$end':([1,4,14,15,18,26,28,31,40,42,43,48,55,75,77,78,82,85,92,94,98,100,110,112,118,119,121,122,126,128,129,130,137,138,139,140,141,142,143,144,145,148,149,],[0,-17,-45,-17,-13,-47,-16,-14,-53,-44,-24,-15,-1,-51,-25,-26,-18,-21,-52,-46,-28,-31,-19,-22,-49,-27,-29,-38,-40,-20,-23,-58,-41,-55,-56,-57,-50,-48,-30,-39,-42,-43,-54,]),'FROM':([2,6,8,19,33,34,69,114,],[5,-2,-5,-3,-4,-6,-8,-7,]),'DISTINCT':([3,25,],[7,39,]),'CADENA':([3,5,7,18,20,21,23,24,25,27,29,30,32,35,39,44,46,47,51,52,53,57,58,59,61,63,64,66,67,68,73,74,79,81,84,96,99,103,104,105,106,107,108,111,113,116,123,132,133,147,],[9,18,9,31,9,34,36,37,38,45,46,47,48,50,54,45,62,65,70,71,72,76,45,45,80,45,83,45,86,87,91,93,45,45,45,118,120,-32,-33,-34,-35,-36,-37,45,45,130,134,76,143,93,]),'MIN':([3,7,20,95,],[11,11,11,11,]),'MAX':([3,7,20,95,],[12,12,12,12,]),'COUNT':([3,7,20,95,],[13,13,13,13,]),'WHERE':([4,14,15,18,28,31,43,48,77,78,82,85,98,100,110,112,119,121,122,126,128,129,137,143,144,145,148,],[-17,27,-17,-13,-16,-14,-24,-15,-25,-26,-18,-21,-28,-31,-19,-22,-27,-29,-38,-40,-20,-23,-41,-30,-39,-42,-43,]),'GROUP':([4,14,15,18,26,28,31,42,43,48,77,78,82,85,98,100,110,112,119,121,122,126,128,129,137,143,144,145,148,],[-17,-45,-17,-13,41,-16,-14,-44,-24,-15,-25,-26,-18,-21,-28,-31,-19,-22,-27,-29,-38,-40,-20,-23,-41,-30,-39,-42,-43,]),'ORDER':([4,14,15,18,26,28,31,40,42,43,48,75,77,78,82,85,94,98,100,110,112,118,119,121,122,126,128,129,137,141,142,143,144,145,148,],[-17,-45,-17,-13,-47,-16,-14,56,-44,-24,-15,-51,-25,-26,-18,-21,-46,-28,-31,-19,-22,-49,-27,-29,-38,-40,-20,-23,-41,-50,-48,-30,-39,-42,-43,]),'PARENTESIS_DERECHO':([4,14,15,18,26,28,31,40,42,43,48,55,70,71,72,75,77,78,82,85,91,92,94,97,98,100,110,112,118,119,121,122,126,128,129,130,135,137,138,139,140,141,142,143,144,145,146,148,149,],[-17,-45,-17,-13,-47,-16,-14,-53,-44,-24,-15,-1,88,89,90,-51,-25,-26,-18,-21,115,-52,-46,119,-28,-31,-19,-22,-49,-27,-29,-38,-40,-20,-23,-58,145,-41,-55,-56,-57,-50,-48,-30,-39,-42,148,-43,-54,]),'INNER':([4,15,18,31,43,48,77,78,82,85,98,100,110,112,119,121,122,126,128,129,137,143,144,145,148,],[16,16,-13,-14,-24,-15,-25,-26,-18,-21,-28,-31,-19,-22,-27,-29,-38,-40,-20,-23,-41,-30,-39,-42,-43,]),'LEFT':([4,15,18,31,43,48,77,78,82,85,98,100,110,112,119,121,122,126,128,129,137,143,144,145,148,],[17,17,-13,-14,-24,-15,-25,-26,-18,-21,-28,-31,-19,-22,-27,-29,-38,-40,-20,-23,-41,-30,-39,-42,-43,]),'COMA':([8,34,69,114,118,130,138,139,140,],[20,-6,-8,-7,132,-58,147,-56,-57,]),'PUNTO':([9,36,37,38,45,54,76,93,120,],[21,51,52,53,61,73,96,116,133,]),'AS':([10,18,34,46,47,88,89,90,115,],[22,32,49,64,67,-9,-10,-11,-12,]),'PARENTESIS_IZQUIERDO':([11,12,13,27,44,58,59,63,66,79,81,84,101,111,113,125,],[23,24,25,44,44,44,44,44,44,44,44,44,124,44,44,136,]),'JOIN':([16,17,],[29,30,]),'COMILLA':([22,49,50,87,99,103,104,105,106,107,108,131,134,],[35,68,69,114,123,-32,-33,-34,-35,-36,-37,123,144,]),'BY':([41,56,],[57,74,]),'AND':([42,43,60,77,78,82,85,97,98,100,110,112,119,121,122,126,128,129,137,143,144,145,148,],[58,-24,58,58,58,58,58,58,-28,-31,58,58,-27,-29,-38,-40,58,58,-41,-30,-39,-42,-43,]),'OR':([42,43,60,77,78,82,85,97,98,100,110,112,119,121,122,126,128,129,137,143,144,145,148,],[59,-24,79,59,59,59,59,59,-28,-31,59,59,-27,-29,-38,-40,59,59,-41,-30,-39,-42,-43,]),'ON':([46,47,62,65,83,86,],[63,66,81,84,111,113,]),'HAVING':([75,118,142,],[95,-49,-48,]),'IN':([80,102,],[101,125,]),'NOT':([80,109,],[102,127,]),'MENOR':([80,88,89,90,115,117,],[103,-9,-10,-11,-12,103,]),'IGUAL':([80,88,89,90,115,117,],[104,-9,-10,-11,-12,104,]),'MAYOR':([80,88,89,90,115,117,],[105,-9,-10,-11,-12,105,]),'MENOR_O_IGUAL':([80,88,89,90,115,117,],[106,-9,-10,-11,-12,106,]),'MAYOR_O_IGUAL':([80,88,89,90,115,117,],[107,-9,-10,-11,-12,107,]),'DISTINTO':([80,88,89,90,115,117,],[108,-9,-10,-11,-12,108,]),'IS':([80,],[109,]),'NUMERO':([99,103,104,105,106,107,108,131,],[122,-32,-33,-34,-35,-36,-37,122,]),'NULL':([109,127,],[126,137,]),'ASC':([130,],[139,]),'DESC':([130,],[140,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'CONS':([0,124,136,],[1,135,146,]),'SELECT_':([0,124,136,],[2,2,2,]),'FROM_':([2,],[4,]),'CAMPOS':([3,7,20,],[6,19,33,]),'CAMPO':([3,7,20,],[8,8,8,]),'FUNCION':([3,7,20,95,],[10,10,10,117,]),'JOIN_':([4,15,],[14,28,]),'ELECCION_JOIN':([4,15,],[15,15,]),'WHERE_':([14,],[26,]),'GROUP_BY':([26,],[40,]),'CONDICION_':([27,44,58,59,63,66,79,81,84,111,113,],[42,60,77,78,82,85,97,110,112,128,129,]),'CONDICION':([27,44,58,59,63,66,79,81,84,111,113,],[43,43,43,43,43,43,43,43,43,43,43,]),'ORDER_BY':([40,],[55,]),'CAMPOS_AGRUPADOS':([57,132,],[75,142,]),'CAMPOS_ORDENADOS':([74,147,],[92,149,]),'HAVING_':([75,],[94,]),'SUBCONS':([80,],[98,]),'OPERADOR_COMPARATIVO':([80,117,],[99,131,]),'NULLABLE':([80,],[100,]),'VALOR':([99,131,],[121,141,]),'ORDEN':([130,],[138,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> CONS","S'",1,None,None,None),
  ('CONS -> SELECT_ FROM_ JOIN_ WHERE_ GROUP_BY ORDER_BY','CONS',6,'p_CONS','Grupo07.py',86),
  ('SELECT_ -> SELECT CAMPOS','SELECT_',2,'p_SELECT_','Grupo07.py',89),
  ('SELECT_ -> SELECT DISTINCT CAMPOS','SELECT_',3,'p_SELECT_','Grupo07.py',90),
  ('CAMPOS -> CAMPO COMA CAMPOS','CAMPOS',3,'p_CAMPOS','Grupo07.py',93),
  ('CAMPOS -> CAMPO','CAMPOS',1,'p_CAMPOS','Grupo07.py',94),
  ('CAMPO -> CADENA PUNTO CADENA','CAMPO',3,'p_CAMPO','Grupo07.py',97),
  ('CAMPO -> CADENA PUNTO CADENA AS COMILLA CADENA COMILLA','CAMPO',7,'p_CAMPO','Grupo07.py',98),
  ('CAMPO -> FUNCION AS COMILLA CADENA COMILLA','CAMPO',5,'p_CAMPO','Grupo07.py',99),
  ('FUNCION -> MIN PARENTESIS_IZQUIERDO CADENA PUNTO CADENA PARENTESIS_DERECHO','FUNCION',6,'p_FUNCION','Grupo07.py',111),
  ('FUNCION -> MAX PARENTESIS_IZQUIERDO CADENA PUNTO CADENA PARENTESIS_DERECHO','FUNCION',6,'p_FUNCION','Grupo07.py',112),
  ('FUNCION -> COUNT PARENTESIS_IZQUIERDO CADENA PUNTO CADENA PARENTESIS_DERECHO','FUNCION',6,'p_FUNCION','Grupo07.py',113),
  ('FUNCION -> COUNT PARENTESIS_IZQUIERDO DISTINCT CADENA PUNTO CADENA PARENTESIS_DERECHO','FUNCION',7,'p_FUNCION','Grupo07.py',114),
  ('FROM_ -> FROM CADENA','FROM_',2,'p_FROM_','Grupo07.py',138),
  ('FROM_ -> FROM CADENA CADENA','FROM_',3,'p_FROM_','Grupo07.py',139),
  ('FROM_ -> FROM CADENA AS CADENA','FROM_',4,'p_FROM_','Grupo07.py',140),
  ('JOIN_ -> ELECCION_JOIN JOIN_','JOIN_',2,'p_JOIN','Grupo07.py',152),
  ('JOIN_ -> <empty>','JOIN_',0,'p_JOIN','Grupo07.py',153),
  ('ELECCION_JOIN -> INNER JOIN CADENA ON CONDICION_','ELECCION_JOIN',5,'p_ELECCION_JOIN','Grupo07.py',156),
  ('ELECCION_JOIN -> INNER JOIN CADENA CADENA ON CONDICION_','ELECCION_JOIN',6,'p_ELECCION_JOIN','Grupo07.py',157),
  ('ELECCION_JOIN -> INNER JOIN CADENA AS CADENA ON CONDICION_','ELECCION_JOIN',7,'p_ELECCION_JOIN','Grupo07.py',158),
  ('ELECCION_JOIN -> LEFT JOIN CADENA ON CONDICION_','ELECCION_JOIN',5,'p_ELECCION_JOIN','Grupo07.py',159),
  ('ELECCION_JOIN -> LEFT JOIN CADENA CADENA ON CONDICION_','ELECCION_JOIN',6,'p_ELECCION_JOIN','Grupo07.py',160),
  ('ELECCION_JOIN -> LEFT JOIN CADENA AS CADENA ON CONDICION_','ELECCION_JOIN',7,'p_ELECCION_JOIN','Grupo07.py',161),
  ('CONDICION_ -> CONDICION','CONDICION_',1,'p_CONDICION_','Grupo07.py',172),
  ('CONDICION_ -> CONDICION_ AND CONDICION_','CONDICION_',3,'p_CONDICION_','Grupo07.py',173),
  ('CONDICION_ -> CONDICION_ OR CONDICION_','CONDICION_',3,'p_CONDICION_','Grupo07.py',174),
  ('CONDICION_ -> PARENTESIS_IZQUIERDO CONDICION_ OR CONDICION_ PARENTESIS_DERECHO','CONDICION_',5,'p_CONDICION_','Grupo07.py',175),
  ('CONDICION_ -> CADENA PUNTO CADENA SUBCONS','CONDICION_',4,'p_CONDICION_','Grupo07.py',176),
  ('CONDICION -> CADENA PUNTO CADENA OPERADOR_COMPARATIVO VALOR','CONDICION',5,'p_CONDICION','Grupo07.py',188),
  ('CONDICION -> CADENA PUNTO CADENA OPERADOR_COMPARATIVO CADENA PUNTO CADENA','CONDICION',7,'p_CONDICION','Grupo07.py',189),
  ('CONDICION -> CADENA PUNTO CADENA NULLABLE','CONDICION',4,'p_CONDICION','Grupo07.py',190),
  ('OPERADOR_COMPARATIVO -> MENOR','OPERADOR_COMPARATIVO',1,'p_OPERADOR_COMPARATIVO','Grupo07.py',218),
  ('OPERADOR_COMPARATIVO -> IGUAL','OPERADOR_COMPARATIVO',1,'p_OPERADOR_COMPARATIVO','Grupo07.py',219),
  ('OPERADOR_COMPARATIVO -> MAYOR','OPERADOR_COMPARATIVO',1,'p_OPERADOR_COMPARATIVO','Grupo07.py',220),
  ('OPERADOR_COMPARATIVO -> MENOR_O_IGUAL','OPERADOR_COMPARATIVO',1,'p_OPERADOR_COMPARATIVO','Grupo07.py',221),
  ('OPERADOR_COMPARATIVO -> MAYOR_O_IGUAL','OPERADOR_COMPARATIVO',1,'p_OPERADOR_COMPARATIVO','Grupo07.py',222),
  ('OPERADOR_COMPARATIVO -> DISTINTO','OPERADOR_COMPARATIVO',1,'p_OPERADOR_COMPARATIVO','Grupo07.py',223),
  ('VALOR -> NUMERO','VALOR',1,'p_VALOR','Grupo07.py',226),
  ('VALOR -> COMILLA CADENA COMILLA','VALOR',3,'p_VALOR','Grupo07.py',227),
  ('NULLABLE -> IS NULL','NULLABLE',2,'p_NULLABLE','Grupo07.py',230),
  ('NULLABLE -> IS NOT NULL','NULLABLE',3,'p_NULLABLE','Grupo07.py',231),
  ('SUBCONS -> IN PARENTESIS_IZQUIERDO CONS PARENTESIS_DERECHO','SUBCONS',4,'p_SUBCONS','Grupo07.py',234),
  ('SUBCONS -> NOT IN PARENTESIS_IZQUIERDO CONS PARENTESIS_DERECHO','SUBCONS',5,'p_SUBCONS','Grupo07.py',235),
  ('WHERE_ -> WHERE CONDICION_','WHERE_',2,'p_WHERE_','Grupo07.py',238),
  ('WHERE_ -> <empty>','WHERE_',0,'p_WHERE_','Grupo07.py',239),
  ('GROUP_BY -> GROUP BY CAMPOS_AGRUPADOS HAVING_','GROUP_BY',4,'p_GROUP_BY','Grupo07.py',242),
  ('GROUP_BY -> <empty>','GROUP_BY',0,'p_GROUP_BY','Grupo07.py',243),
  ('CAMPOS_AGRUPADOS -> CADENA PUNTO CADENA COMA CAMPOS_AGRUPADOS','CAMPOS_AGRUPADOS',5,'p_CAMPOS_AGRUPADOS','Grupo07.py',246),
  ('CAMPOS_AGRUPADOS -> CADENA PUNTO CADENA','CAMPOS_AGRUPADOS',3,'p_CAMPOS_AGRUPADOS','Grupo07.py',247),
  ('HAVING_ -> HAVING FUNCION OPERADOR_COMPARATIVO VALOR','HAVING_',4,'p_HAVING_','Grupo07.py',258),
  ('HAVING_ -> <empty>','HAVING_',0,'p_HAVING_','Grupo07.py',259),
  ('ORDER_BY -> ORDER BY CAMPOS_ORDENADOS','ORDER_BY',3,'p_ORDER_BY','Grupo07.py',262),
  ('ORDER_BY -> <empty>','ORDER_BY',0,'p_ORDER_BY','Grupo07.py',263),
  ('CAMPOS_ORDENADOS -> CADENA PUNTO CADENA ORDEN COMA CAMPOS_ORDENADOS','CAMPOS_ORDENADOS',6,'p_CAMPOS_ORDENADOS','Grupo07.py',266),
  ('CAMPOS_ORDENADOS -> CADENA PUNTO CADENA ORDEN','CAMPOS_ORDENADOS',4,'p_CAMPOS_ORDENADOS','Grupo07.py',267),
  ('ORDEN -> ASC','ORDEN',1,'p_ORDEN','Grupo07.py',278),
  ('ORDEN -> DESC','ORDEN',1,'p_ORDEN','Grupo07.py',279),
  ('ORDEN -> <empty>','ORDEN',0,'p_ORDEN','Grupo07.py',280),
]
