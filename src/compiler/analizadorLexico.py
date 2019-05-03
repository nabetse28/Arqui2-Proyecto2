import ply.lex as lex
import re
import codecs
import os
import sys

clase = 0

errL = False
isComment = 0

# Tokens para catalogar los lexemas
tokens = ['ID', 'RPC', 'LPC', 'NUMBER', 'REG',
          'VEC', 'COMMA', 'MINUS', 'NUM', 'DP']


kword = ['ADD', 'SUB', 'MOV', 'NOP', 'STR', 'LDR', 'CMP', 'ADDV',
         'SUBV', 'MOVV', 'XORV', 'CIRRV', 'CIRLV', 'ALGV', 'STRV', 'LDRV', 'REPEAT']


tokens = tokens + kword

# This are the tokens

t_RPC = r'\]'
t_LPC = r'\['
t_COMMA = r','
t_MINUS = r'\-'
t_NUM = r'\#'
t_DP = r'\:'


def t_MOVV(t):
    r'MOVV|movv'
    t.value = t.value.upper()
    return t


def t_XORV(t):
    r'XORV|xorv'
    t.value = t.value.upper()
    return t


def t_CIRRV(t):
    r'CIRRV|cirrv'
    t.value = t.value.upper()
    return t


def t_CIRLV(t):
    r'CIRLV|cirlv'
    t.value = t.value.upper()
    return t


def t_ALGV(t):
    r'ALGV|algv'
    t.value = t.value.upper()
    return t


def t_STRV(t):
    r'STRV|strv'
    t.value = t.value.upper()
    return t


def t_LDRV(t):
    r'LDRV|ldrv'
    t.value = t.value.upper()
    return t


def t_CMP(t):
    r'CMP|cmp'
    t.value = t.value.upper()
    return t


def t_ADDV(t):
    r'ADDV|addv'
    t.value = t.value.upper()
    return t


def t_SUBV(t):
    r'SUBV|subv'
    t.value = t.value.upper()
    return t


def t_ADD(t):
    r'ADD|add'
    t.value = t.value.upper()
    return t


def t_SUB(t):
    r'SUB|sub'
    t.value = t.value.upper()
    return t


def t_MOV(t):
    r'MOV|mov'
    t.value = t.value.upper()
    return t


def t_NOP(t):
    r'NOP|nop'
    t.value = t.value.upper()
    return t


def t_STR(t):
    r'STR|str'
    t.value = t.value.upper()
    return t


def t_LDR(t):
    r'LDR|ldr'
    t.value = t.value.upper()
    return t


def t_ID(t):
    r'[a-qs-uw-zA-QS-UW-Z][a-zA-Z0-9]*'
    return t


def t_REG(t):
    r'[rR][0-9]+'
    t.value = t.value.upper()
    return t


def t_VEC(t):
    r'[vV][0-9]+'
    t.value = t.value.upper()
    return t


def t_COMMENT(t):
    r';.*'
    global isComment
    isComment += 1
    t.lexer.skip(1)


def t_NUMBER(t):
    r'\d+|\-\d+'
    return t


def t_error(t):
    global errL
    errL = True
    print("Here is an error", t.value[0])
    t.lexer.skip(1)


def t_nonespace(t):
    r'\s+'
    pass


def getErrL():
    global errL
    return errL
