import ply.yacc as yacc
import os
import codecs
import time
import re
from analizadorLexico import *

precedence = (('left', 'RPC', 'LPC'))

precedence = (
    ('left', 'ID', 'NUMBER'),
    ('left', 'REG', 'COMMA'),
    ('left', 'RPC', 'LPC')
)

listap = {}
errS = False


def p_program(p):  # LISTO##LISTO#
    '''program : block'''
    p[0] = {1: p[1]}
    global listap
    listap = p[0]


def p_block(p):  # LISTO##LISTO#
    '''block : inst block'''
    p[0] = {1: p[1], 2: p[2]}


def p_blockEmpty(p):  # LISTO##LISTO#
    '''block : empty'''
    p[0] = {1: "NULL"}


def p_instTag(p):  # LISTO##LISTO#
    '''inst : ID DP'''
    p[0] = {1: "TAG", 2: p[1], 3: "END"}


def p_instNop(p):  # LISTO##LISTO#
    '''inst : NOP'''
    p[0] = {1: "NOP", 2: "END"}

##################### Basic Instructions #####################


def p_instMOVImm(p):
    '''inst : MOV REG COMMA NUM NUMBER'''
    p[4] = int(p[5])
    p[0] = {1: "MOV", 2: p[2], 3: p[5], 4: "END"}


def p_instMOVReg(p):
    '''inst : MOV REG COMMA REG COMMA REG'''
    p[0] = {1: "MOV", 2: p[2], 3: p[4], 4: p[6], 5: "END"}


def p_instAdd(p):  # LISTO##LISTO#
    '''inst : ADD REG COMMA REG COMMA REG'''
    p[0] = {1: "ADD", 2: p[2], 3: p[4], 4: p[6], 5: "END"}


def p_instAddImm1(p):  # LISTO##LISTO#
    '''inst : ADD REG COMMA REG COMMA NUM NUMBER'''
    p[6] = int(p[7])
    p[0] = {1: "ADDI", 2: p[2], 3: p[4], 4: p[7], 5: "END"}


def p_instSub(p):  # LISTO##LISTO#
    '''inst : SUB REG COMMA REG COMMA REG'''
    p[0] = {1: "SUB", 2: p[2], 3: p[4], 4: p[6], 5: "END"}


def p_instSubImm(p):  # LISTO##LISTO#
    '''inst : SUB REG COMMA REG COMMA NUM NUMBER'''
    p[6] = int(p[7])
    p[0] = {1: "SUBI", 2: p[2], 3: p[4], 4: p[7], 5: "END"}


def p_instLdrR(p):  # LISTO##LISTO#
    '''inst : LDR REG COMMA LPC REG RPC COMMA REG'''
    p[0] = {1: "LDRR", 2: p[2], 3: p[5], 4: p[8], 5: "END"}


def p_instLdrMR(p):  # LISTO##LISTO#
    '''inst : LDR REG COMMA LPC REG RPC COMMA MINUS REG'''
    p[0] = {1: "LDR-R", 2: p[2], 3: p[5], 4: p[9], 5: "END"}


def p_instLdrImm(p):  # LISTO##LISTO#
    '''inst : LDR REG COMMA LPC REG RPC COMMA NUM NUMBER'''
    p[9] = int(p[9])
    p[0] = {1: "LDRI", 2: p[2], 3: p[5], 4: int(p[9]), 5: "END"}


def p_instLdrRI(p):  # LISTO##LISTO#
    '''inst : LDR REG COMMA LPC REG COMMA NUM NUMBER RPC'''
    p[0] = {1: "LDRRI", 2: p[2], 3: p[5], 4: p[8], 5: "END"}


def p_instLdr(p):  # LISTO##LISTO#
    '''inst : LDR REG COMMA LPC REG RPC'''
    p[0] = {1: "LDR", 2: p[2], 3: p[5], 4: 0, 5: "END"}


def p_instStrR(p):  # LISTO##LISTO#
    '''inst : STR REG COMMA LPC REG RPC COMMA REG'''
    p[0] = {1: "STRR", 2: p[2], 3: p[5], 4: p[8], 5: "END"}


def p_instStrRI(p):  # LISTO##LISTO#
    '''inst : STR REG COMMA LPC REG COMMA NUM NUMBER RPC'''
    p[0] = {1: "STRRI", 2: p[2], 3: p[5], 4: p[8], 5: "END"}


def p_instStrMR(p):  # LISTO##LISTO#
    '''inst : STR REG COMMA LPC REG RPC COMMA MINUS REG'''
    p[0] = {1: "STR-R", 2: p[2], 3: p[5], 4: p[9], 5: "END"}


def p_instStrImm(p):  # LISTO##LISTO#
    '''inst : STR REG COMMA LPC REG RPC COMMA NUM NUMBER'''
    p[9] = int(p[9])
    p[0] = {1: "STRI", 2: p[2], 3: p[5], 4: (p[9]), 5: "END"}


def p_instStr(p):  # LISTO##LISTO#
    '''inst : STR REG COMMA LPC REG RPC'''
    p[0] = {1: "STR", 2: p[2], 3: p[5], 4: 0, 5: "END"}


##################### Vectorial Instructions #####################


def p_instAddVec(p):
    '''inst : ADDV VEC COMMA VEC COMMA VEC'''
    p[0] = {1: "ADDV", 2: p[2], 3: p[4], 4: p[6], 5: "END"}


def p_instAddVecImm(p):
    '''inst : ADDV VEC COMMA NUM NUMBER'''
    p[0] = {1: "ADDVI", 2: p[2], 3: int(p[5]), 4: "END"}


def p_instSubVec(p):
    '''inst : SUBV VEC COMMA VEC COMMA VEC'''
    p[0] = {1: "SUBV", 2: p[2], 3: p[4], 4: p[6], 5: "END"}


def p_instSubVecImm(p):
    '''inst : ADDV VEC COMMA NUM NUMBER'''
    p[0] = {1: "SUBVI", 2: p[2], 3: int(p[5]), 4: "END"}


##################### Other Instructions #####################


def p_empty(p):  # LISTO#
    '''empty :'''
    pass


def p_error(p):  # LISTO#
    global errS
    errS = True
    print("Error de sintaxis: ", str(p))


def recorrer(d):
    global SemanticList
    list(d.keys()).sort()
    for x in list(d.keys()):
        if (isinstance(d[x], dict)):
            recorrer(d[x])
        else:
            if(d[x] != "NULL"):
                SemanticList += [d[x]]


def getErrS():
    global errS
    return errS


def divInst(lista):
    c = 0
    r = []
    for x in range(len(lista)):
        if lista[x] == 'END':
            r.append(lista[c:x])
            c = x+1
    return r


SemanticList = []


def initCompi(nameDoc):
    fp = codecs.open(nameDoc, "r", "utf-8")
    cadena = fp.read()
    print(cadena)
    fp.close()
    analizador = lex.lex()
    analizador.input(cadena)

    parser = yacc.yacc()
    result = parser.parse(cadena)

    global SemanticList
    recorrer(listap)
    return divInst(SemanticList)
