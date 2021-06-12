import sys
import ply.lex as lex

reservado = {
	'SELECT':'SELECT',
	'FROM':'FROM',
	'INNER':'INNER',
	'JOIN':'JOIN',
	'LEFT':'LEFT',
	'AS':'AS',
	'WHERE':'WHERE',
	'IN':'IN',
	'GROUP':'GROUP',
	'BY':'BY',
	'HAVING':'HAVING',
	'ORDER':'ORDER',
	'MIN':'MIN',
	'MAX':'MAX',
	'COUNT':'COUNT',
	'DISTINCT':'DISTINCT',
	'AND':'AND',
	'OR':'OR',
	'ON':'ON',
	'IS':'IS',
	'NULL':'NULL',
	'NOT':'NOT',
	'ASC':'ASC',
	'DESC':'DESC',}

tokens = [
	'NUMERO',
	'CADENA',
	'MENOR',
	'IGUAL',
	'MAYOR',
	'MENOR_O_IGUAL',
	'MAYOR_O_IGUAL',
	'DISTINTO',
	'PUNTO',
	'COMA',
	'COMILLA',
	'PARENTESIS_IZQUIERDO',
	'PARENTESIS_DERECHO',] + list(reservado.values())

t_MENOR = r'<'
t_IGUAL = r'='
t_MAYOR = r'>'
t_MENOR_O_IGUAL = r'<='
t_MAYOR_O_IGUAL = r'>='
t_DISTINTO = r'<>'
t_PUNTO = r'\.'
t_COMA = r','
t_COMILLA = r"'"
t_PARENTESIS_IZQUIERDO = r'\('
t_PARENTESIS_DERECHO = r'\)'


def t_NUMERO(t):
	r'\d+'
	t.type = reservado.get(t.value, 'NUMERO')
	t.value = int(t.value)
	return t

def t_CADENA(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	t.type = reservado.get(t.value, 'CADENA')
	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)

lexer = lex.lex()

Tablas = {}
Columnas = {}


def p_CONS(p):
	'''CONS : SELECT_ FROM_ JOIN_ WHERE_ GROUP_BY ORDER_BY'''

def p_SELECT_(p):
	'''SELECT_ : SELECT CAMPOS
	| SELECT DISTINCT CAMPOS'''

def p_CAMPOS(p):
	'''CAMPOS : CAMPO COMA CAMPOS
	| CAMPO'''

def p_CAMPO(p):
	'''CAMPO : CADENA PUNTO CADENA
	| CADENA PUNTO CADENA AS COMILLA CADENA COMILLA
	| FUNCION AS COMILLA CADENA COMILLA'''

	key = p[1]
	if len(p) != 6:
		if key in Columnas:
			columna = p[3]
			if columna not in Columnas[key]:
				Columnas[key].append(columna)
		else:		
			Columnas[key] = [p[3]]

def p_FUNCION(p):
	'''FUNCION : MIN PARENTESIS_IZQUIERDO CADENA PUNTO CADENA PARENTESIS_DERECHO
	| MAX PARENTESIS_IZQUIERDO CADENA PUNTO CADENA PARENTESIS_DERECHO
	| COUNT PARENTESIS_IZQUIERDO CADENA PUNTO CADENA PARENTESIS_DERECHO
	| COUNT PARENTESIS_IZQUIERDO DISTINCT CADENA PUNTO CADENA PARENTESIS_DERECHO'''

	key = ''
	if len(p) < 8:
		key = p[3]
	else:
		key = p[4]
	if len(p) == 7:
		if key in Columnas:
			columna = p[5]
			if columna not in Columnas[key]:
				Columnas[key].append(columna)
		else:
			Columnas[key] = [p[5]]
	else:
		if key in Columnas:
			columna = p[6]
			if columna not in Columnas[key]:
				Columnas[key].append(columna)
		else:
			Columnas[key] = [p[6]]

def p_FROM_(p):
	'''FROM_ : FROM CADENA
	| FROM CADENA CADENA
	| FROM CADENA AS CADENA'''

	key = p[2]
	if len(p) == 3:
		Tablas[key] = key
	elif len(p) == 4:
		Tablas[key] = p[3]
	else:
		Tablas[key] = p[4]


def p_JOIN(p):
	''' JOIN_ : ELECCION_JOIN JOIN_
	| '''

def p_ELECCION_JOIN(p):
	''' ELECCION_JOIN : INNER JOIN CADENA ON CONDICION_
	| INNER JOIN CADENA CADENA ON CONDICION_
	| INNER JOIN CADENA AS CADENA ON CONDICION_
	| LEFT JOIN CADENA ON CONDICION_
	| LEFT JOIN CADENA CADENA ON CONDICION_
	| LEFT JOIN CADENA AS CADENA ON CONDICION_ '''

	key = p[3]
	if len(p) == 6:
		Tablas[key] = key
	elif len(p) == 7:
		Tablas[key] = p[4]
	else:
		Tablas[key] = p[5]

def p_CONDICION_(p):
	'''CONDICION_ : CONDICION
	| CONDICION_ AND CONDICION_
	| CONDICION_ OR CONDICION_
	| PARENTESIS_IZQUIERDO CONDICION_ OR CONDICION_ PARENTESIS_DERECHO
	| CADENA PUNTO CADENA SUBCONS '''

	if len(p) == 5:
		key = p[1]
		if key in Columnas:
			columna = p[3]
			if columna not in Columnas[key]:
				Columnas[key].append(columna)
		else:
			Columnas[key] = [p[3]]

def p_CONDICION(p):
	''' CONDICION : CADENA PUNTO CADENA OPERADOR_COMPARATIVO VALOR
	| CADENA PUNTO CADENA OPERADOR_COMPARATIVO CADENA PUNTO CADENA
	| CADENA PUNTO CADENA NULLABLE '''

	if len(p) == 8:
		key1 = p[1]
		key2 = p[5]
		if key1 in Columnas:
			columna = p[3]
			if columna not in Columnas[key1]:
				Columnas[key1].append(columna)
		else:
			Columnas[key1] = [p[3]]
		if key2 in Columnas:
			columna = p[7]
			if columna not in Columnas[key2]:
				Columnas[key2].append(columna)
		else:
			Columnas[key2] = [p[7]]
	else:
		key = p[1]
		if key in Columnas:
			columna = p[3]
			if columna not in Columnas[key]:
				Columnas[key].append(columna)
		else:
			Columnas[key] = [p[3]]


def p_OPERADOR_COMPARATIVO(p):
	''' OPERADOR_COMPARATIVO : MENOR
	| IGUAL
	| MAYOR
	| MENOR_O_IGUAL
	| MAYOR_O_IGUAL
	| DISTINTO '''

def p_VALOR(p):
	'''VALOR : NUMERO
	| COMILLA CADENA COMILLA'''

def p_NULLABLE(p):
	''' NULLABLE : IS NULL
	| IS NOT NULL'''

def p_SUBCONS(p): 
	'''SUBCONS : IN PARENTESIS_IZQUIERDO CONS PARENTESIS_DERECHO
	| NOT IN PARENTESIS_IZQUIERDO CONS PARENTESIS_DERECHO'''

def p_WHERE_(p):
	'''WHERE_ : WHERE CONDICION_
	| '''

def p_GROUP_BY(p):
	'''GROUP_BY : GROUP BY CAMPOS_AGRUPADOS HAVING_
	| '''

def p_CAMPOS_AGRUPADOS(p):
	'''CAMPOS_AGRUPADOS : CADENA PUNTO CADENA COMA CAMPOS_AGRUPADOS
	| CADENA PUNTO CADENA'''

	key = p[1]
	if key in Columnas:
		columna = p[3]
		if columna not in Columnas[key]:
			Columnas[key].append(columna)
	else:
		Columnas[key] = [p[3]]

def p_HAVING_(p):
	'''HAVING_ : HAVING FUNCION OPERADOR_COMPARATIVO VALOR
	| '''

def p_ORDER_BY(p):
	'''ORDER_BY : ORDER BY CAMPOS_ORDENADOS
	| '''

def p_CAMPOS_ORDENADOS(p):
	'''CAMPOS_ORDENADOS : CADENA PUNTO CADENA ORDEN COMA CAMPOS_ORDENADOS
	| CADENA PUNTO CADENA ORDEN'''

	key = p[1]
	if key in Columnas:
		columna = p[3]
		if columna not in Columnas[key]:
			Columnas[key].append(columna)
	else:
		Columnas[key] = [p[3]]

def p_ORDEN(p):
	'''ORDEN : ASC
	| DESC
	| '''

def p_error(p):
	if p:
		print("Syntax error at '%s'" % p.value)
	else:
		print("Syntax error at EOF")

import ply.yacc as yacc

def parse_select_statement(s):
	Tablas.clear()
	Columnas.clear()
	cont = 0
	yacc.yacc()
	yacc.parse(s)
	ADevolver = {}
	for keyTabla in Tablas:
		Tabla_o_Alias = Tablas.get(keyTabla)
		if Columnas.get(Tabla_o_Alias) is not None:
			ADevolver[keyTabla] = sorted(Columnas.get(Tabla_o_Alias))
			cont += 1
	if len(Columnas.keys()) > cont:
		raise Exception('Error: Actualmente hay mas llaves en el diccionario Columnas que matchs encontrados de columnas y tablas, revise el uso de alias en tablas e intente nuevamente')
	return ADevolver
