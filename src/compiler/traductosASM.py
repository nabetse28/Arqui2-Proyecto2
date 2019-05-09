from analizadorSintactico import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename
tags = {}
errT = False


def comp2(dn):
    n = len(bin(abs(int(dn)))[2:])
    r = bin(abs(int(2**n-dn)))[2:]
    while(len(r) < len(bin(abs(int(dn)))[2:])):
        r = '0'+r
    return r


def ext(n, c, e):
    while(len(n) != c):
        if(len(n) > c):
            n = n[1:]
        else:
            n = e+n
    return n


def getImmBr(aL, tL):
    i = 0
    flag = False
    while(aL != tL):
        if(aL > tL):
            i -= 1
            aL -= 1
        else:
            flag = True
            i += 1
            aL += 1
    return i


def traducir(l):
    global tags
    global errT

    inst = []
    cL = -1
    regs = {'R0': '0000', 'R1': '0001',
            'R2': '0010', 'R3': '0011',
            'R4': '0100', 'R5': '0101',
            'R6': '0110', 'R7': '0111',
            'R8': '1000', 'R9': '1001',
            'R10': '1010', 'R11': '1011',
            'R12': '1100', 'R13': '1101',
            'R14': '1110', 'R15': '1111'}

    vecs = {'V0': '0000', 'V1': '0001',
            'V2': '0010', 'V3': '0011',
            'V4': '0100', 'V5': '0101',
            'V6': '0110', 'V7': '0111',
            'V8': '1000', 'V9': '1001',
            'V10': '1010', 'V11': '1011',
            'V12': '1100', 'V13': '1101',
            'V14': '1110', 'V15': '1111'}
    for x in l:
        inst.append(x)

    # for x in inst:
    #     cL += 1
    #     if(x[0] == 'TAG'):
    #         if(x[1] in list(tags.keys())):
    #             errT = True
    #         tags[x[1]] = cL
    #         cL -= 1
    cM = []
    repeat_x = 0
    repeat_y = 0
    repeat = []
    for x in inst:
        if(x[0] == "REPEAT"):
            for x in range(0, x[1]):
                for y in range(repeat_y, repeat_x):
                    repeat.append(inst[y])

            repeat_y = repeat_x + 1

        repeat_x += 1

    # print(repeat)

    for x in repeat:
        print(x)

    # cL = -1
    for x in repeat:

        ################## SCALAR ##################
        if(x[0] == 'ADD'):
            i = '1110'  # COND
            i += '00'  # OP
            i += '0'  # I
            i += '0'  # V if vector
            i += '0100'  # CMD
            i += regs[x[2]]
            i += regs[x[1]]
            i += '00000000'
            i += regs[x[3]]
            cM += [i]
        elif(x[0] == 'ADDI'):
            if(int(x[3]) >= 0):
                i = '1110'  # COND
                i += '00'  # OP
                i += '1'  # I
                i += '0'  # V if vector
                i += '0100'  # CMD
            else:
                i = '1110'  # COND
                i += '00'  # OP
                i += '1'  # I
                i += '0'  # V if vector
                i += '0010'  # CMD
            i += regs[x[2]]
            i += regs[x[1]]
            i += '0000'
            i += ext(bin(abs(int(x[3])))[2:], 8, '0')
            cM += [i]
        elif(x[0] == 'SUB'):
            i = '1110'  # COND
            i += '00'  # OP
            i += '0'  # I
            i += '0'  # V if vector
            i += '0010'  # CMD
            i += regs[x[2]]
            i += regs[x[1]]
            i += '00000000'
            i += regs[x[3]]
            cM += [i]
        elif(x[0] == 'SUBI'):
            if(int(x[3]) >= 0):
                i = '1110'  # COND
                i += '00'  # OP
                i += '1'  # I
                i += '0'  # V if vector
                i += '0010'  # CMD
            else:
                i = '1110'  # COND
                i += '00'  # OP
                i += '1'  # I
                i += '0'  # V if vector
                i += '0100'  # CMD
            i += regs[x[2]]
            i += regs[x[1]]
            i += '0000'
            i += ext(bin(abs(int(x[3])))[2:], 8, '0')
            cM += [i]

        elif(x[0] == 'LDRI'):
            i = '111001'
            i += '0'  # I'
            i += '0'  # P
            if(int(x[3]) >= 0):
                i += '1'  # U
            else:
                i += '0'  # U
            i += '0'  # B
            i += '0'  # W
            i += '1'  # L
            i += regs[x[2]]
            i += regs[x[1]]
            i += ext(bin(abs(int(x[3])))[2:], 12, '0')
            cM += [i]
        elif(x[0] == 'LDRRI'):
            i = '111001'
            i += '0'  # I'
            i += '1'  # P
            if(int(x[3]) >= 0):
                i += '1'  # U
            else:
                i += '0'  # U
            i += '0'  # B
            i += '0'  # W
            i += '1'  # L
            i += regs[x[2]]
            i += regs[x[1]]
            i += ext(bin(abs(int(x[3])))[2:], 12, '0')
            cM += [i]
        elif(x[0] == 'LDR'):
            i = '111001'
            i += '0'  # I'
            i += '1'  # P
            i += '1'  # U
            i += '0'  # B
            i += '0'  # W
            i += '1'  # L
            i += regs[x[2]]
            i += regs[x[1]]
            i += ext(bin(0)[2:], 12, '0')
            cM += [i]
        elif(x[0] == 'STRI'):
            i = '111001'
            i += '0'  # I'
            i += '0'  # P
            if(int(x[3]) >= 0):
                i += '1'  # U
            else:
                i += '0'  # U
            i += '0'  # B
            i += '0'  # W
            i += '0'  # L
            i += regs[x[2]]
            i += regs[x[1]]
            i += ext(bin(abs(int(x[3])))[2:], 12, '0')
            cM += [i]
        elif(x[0] == 'STRRI'):
            i = '111001'
            i += '0'  # I'
            i += '1'  # P
            if(int(x[3]) >= 0):
                i += '1'  # U
            else:
                i += '0'  # U
            i += '0'  # B
            i += '0'  # W
            i += '0'  # L
            i += regs[x[2]]
            i += regs[x[1]]
            i += ext(bin(abs(int(x[3])))[2:], 12, '0')
            cM += [i]
        elif(x[0] == 'STR'):
            i = '111001'
            i += '0'  # I'
            i += '1'  # P
            i += '1'  # U
            i += '0'  # B
            i += '0'  # W
            i += '0'  # L
            i += regs[x[2]]
            i += regs[x[1]]
            i += ext(bin(0)[2:], 12, '0')
            cM += [i]

################## VECTORS ##################
        elif(x[0] == 'ADDV'):
            i = '1110'  # COND
            i += '00'  # OP
            i += '0'  # I
            i += '1'  # V if vector
            i += '0100'  # CMD
            i += vecs[x[2]]  # Rn
            i += vecs[x[1]]  # Rd
            i += '00000000'  # Src
            i += vecs[x[3]]  # Src vector

            cM += [i]
        elif(x[0] == 'ADDVI'):
            if(int(x[3]) >= 0):
                i = '1110'  # COND
                i += '00'  # OP
                i += '1'  # I
                i += '1'  # V if vector
                i += '0100'  # CMD
            else:
                i = '1110'  # COND
                i += '00'  # OP
                i += '1'  # I
                i += '1'  # V if vector
                i += '0010'  # CMD
            i += vecs[x[2]]  # Rn
            i += vecs[x[1]]  # Rd
            i += ext(bin(0)[2:], 12, '0')
            cM += [i]
        elif(x[0] == 'SUBV'):
            i = '1110'  # COND
            i += '00'  # OP
            i += '0'  # I
            i += '1'  # V if vector
            i += '0010'  # CMD
            i += vecs[x[2]]  # Rn
            i += vecs[x[1]]  # Rd
            i += '00000000'  # Src
            i += vecs[x[3]]  # Src vector
            cM += [i]
        elif(x[0] == 'SUBVI'):
            if(int(x[3]) >= 0):
                i = '1110'  # COND
                i += '00'  # OP
                i += '1'  # I
                i += '1'  # V if vector
                i += '0010'  # CMD
            else:
                i = '1110'  # COND
                i += '00'  # OP
                i += '1'  # I
                i += '1'  # V if vector
                i += '0100'  # CMD
            i += vecs[x[2]]  # Rn
            i += vecs[x[1]]  # Rd
            i += ext(bin(0)[2:], 12, '0')
            cM += [i]
        elif(x[0] == 'CIRRV'):
            i = '1110'  # COND
            i += '00'  # OP
            i += '0'  # I
            i += '1'  # V if vector
            i += '1000'  # CMD
            i += vecs[x[2]]  # Rn
            i += vecs[x[1]]  # Rd
            i += '00000000'  # Src
            i += vecs[x[3]]  # Src vector
            cM += [i]
        elif(x[0] == 'CIRRVI'):
            i = '1110'  # COND
            i += '00'  # OP
            i += '1'  # I
            i += '1'  # V if vector
            i += '1000'  # CMD
            i += vecs[x[2]]  # Rn
            i += vecs[x[1]]  # Rd
            i += ext(bin(abs(int(x[3])))[2:], 12, '0')
            cM += [i]
        elif(x[0] == 'CIRLV'):
            i = '1110'  # COND
            i += '00'  # OP
            i += '0'  # I
            i += '1'  # V if vector
            i += '1001'  # CMD
            i += vecs[x[2]]  # Rn
            i += vecs[x[1]]  # Rd
            i += '00000000'  # Src
            i += vecs[x[3]]  # Src vector
            cM += [i]
        elif(x[0] == 'CIRLVI'):
            i = '1110'  # COND
            i += '00'  # OP
            i += '1'  # I
            i += '1'  # V if vector
            i += '1001'  # CMD
            i += vecs[x[2]]  # Rn
            i += vecs[x[1]]  # Rd
            i += ext(bin(abs(int(x[3])))[2:], 12, '0')
            cM += [i]
        elif(x[0] == 'XORV'):
            i = '1110'  # COND
            i += '00'  # OP
            i += '0'  # I
            i += '1'  # V if vector
            i += '0001'  # CMD
            i += vecs[x[2]]  # Rn
            i += vecs[x[1]]  # Rd
            i += '00000000'  # Src
            i += vecs[x[3]]  # Src vector
            cM += [i]
        elif(x[0] == 'XORVI'):
            i = '1110'  # COND
            i += '00'  # OP
            i += '1'  # I
            i += '1'  # V if vector
            i += '0001'  # CMD
            i += vecs[x[2]]  # Rn
            i += vecs[x[1]]  # Rd
            i += ext(bin(abs(int(x[3])))[2:], 12, '0')
            cM += [i]
        # elif(x[0] == 'ALGV'):
        elif(x[0] == 'LDRVRI'):
            i = '1110'
            i += '01'  # op
            i += '0'  # I
            i += '1'  # P
            if(int(x[3]) >= 0):
                i += '1'  # U
            else:
                i += '0'  # U
            i += '1'  # V
            i += '0'  # W
            i += '1'  # L
            i += regs[x[2]]
            i += regs[x[1]]
            i += ext(bin(abs(int(x[3])))[2:], 12, '0')
            cM += [i]
        # elif(x[0] == 'LDRVIO'):
        elif(x[0] == 'STRVRI'):
            i = '1110'
            i += '01'  # op
            i += '0'  # I
            i += '1'  # P
            if(int(x[3]) >= 0):
                i += '1'  # U
            else:
                i += '0'  # U
            i += '1'  # V
            i += '0'  # W
            i += '0'  # L
            i += regs[x[2]]
            i += regs[x[1]]
            i += ext(bin(abs(int(x[3])))[2:], 12, '0')
            cM += [i]
        # elif(x[0] == 'STRVIO'):

        else:
            print(x[0])
            errT = True

        # print(cM)

    return cM


def toHex(b):
    r = []
    for x in b:
        r += [ext(hex(int(x, 2))[2:], 8, '0')]
    return r


def initTrans():
    global errT
    global tags
    tags = {}
    errT = False
    Tk().withdraw()
    filename = askopenfilename()
    c = initCompi(filename)
    print(c)

    b = traducir(c)
    # h = toHex(b)

    if not(getErrL() or getErrS() or errT):
        p = open('codeBin.rs', 'w')

        for x in b:
            print(x)
            p.write(x + "\n")

        p.close()
        # f.close()
        input("Compilacion exitosa")
    else:
        input("Error en compilacion")


try:
    initTrans()
except:
    input("No se encontro el archivo")
