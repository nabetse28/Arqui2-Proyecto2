from PIL import Image
import threading
import time

clock = 1

FLAG_PROCESSOR = True
A = 0
RD = 0
WE = 0
PC = '00000000000000000000000000000000'
PCF = '00000000000000000000000000000000'
INSTF = ''
INSTD = ''
ALURESULTE = ''


RD1 = ''
RD2 = ''
RDV1 = ''
RDV2 = ''

OP = ''
L = ''
IMMEDIATE_NEED = ''
VECTORS_NEED = ''
IMMEDIATE = ''
RD = ''
CMD = ''

IMMEDIATE_NEED_E = ''
VECTORS_NEED_E = ''
OP_E = ''
CMD_E = ''
L_E = ''
RD1_E = ''
RD2_E = ''
RDV1_E = ''
RDV2_E = ''
RD_E=  ''
IMMEDIATE_E = ''

ALURESULTE = ''
WRITEDATAE = ''
WA3E = ''
OPE = ''
CMDE = ''
LE = ''
IMMEDIATE_NEEDE = ''
VECTORS_NEEDE = ''
RD1E = ''
RD2E = ''
RDV1E = ''
RDV2E = ''
READE = ''

ALURESULT_M = ''
WRITEDATA_M = ''
WA3_M = ''
IMMEDIATE_NEED_M = ''
VECTORS_NEED_M = ''
OP_M = ''
CMD_M = ''
L_M = ''
RD1_M = ''
RD2_M = ''
RDV1_M = ''
RDV2_M = ''
RD_M =  ''
IMMEDIATE_M = ''
READ_M = ''

ALURESULTM = ''
WRITEDATAM = ''
WA3M = ''
IMMEDIATE_NEEDM = ''
VECTORS_NEEDM = ''
OPM = ''
CMDM = ''
LM = ''
RD1M = ''
RD2M = ''
RDV1M = ''
RDV2M = ''
RDM =  ''
IMMEDIATEM = ''
READM = ''

ALURESULT_W = ''
WA3_W = ''
IMMEDIATE_NEED_W = ''
VECTORS_NEED_W = ''
OP_W = ''
CMD_W = ''
L_W = ''

MEMORY_ARRAY = []
INSTRUCTION_MEMORY = []
INSTRUCTION_MEMORY_SIZE = 0
REGISTERS = {"0000": [['00000000'], ['00000000'], ['00000000'], ['00000000']], 
             "0001": [['00000000'], ['00000000'], ['00000000'], ['00000000']], 
             "0010": [['00000000'], ['00000000'], ['00000000'], ['00000000']], 
             "0011": [['00000000'], ['00000000'], ['00000000'], ['00000000']],
             "0100": [['00000000'], ['00000000'], ['00000000'], ['00000000']], 
             "0101": [['00000000'], ['00000000'], ['00000000'], ['00000000']], 
             "0110": [['00000000'], ['00000000'], ['00000000'], ['00000000']], 
             "0111": [['00000000'], ['00000000'], ['00000000'], ['00000000']],
             "1000": [['00000000'], ['00000000'], ['00000000'], ['00000000']], 
             "1001": [['00000000'], ['00000000'], ['00000000'], ['00000000']], 
             "1010": [['00000000'], ['00000000'], ['00000000'], ['00000000']], 
             "1011": [['00000000'], ['00000000'], ['00000000'], ['00000000']],
             "1100": [['00000000'], ['00000000'], ['00000000'], ['00000000']], 
             "1101": [['00000000'], ['00000000'], ['00000000'], ['00000000']], 
             "1110": [['00000000'], ['00000000'], ['00000000'], ['00000000']], 
             "1111": [['00000000'], ['00000000'], ['00000000'], ['00000000']]}

VECTORS = {"0000": [['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000']], 
           "0001": [['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000']], 
           "0010": [['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000']], 
           "0011": [['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000']],
           "0100": [['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000']], 
           "0101": [['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000']], 
           "0110": [['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000']], 
           "0111": [['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000']],
           "1000": [['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000']], 
           "1001": [['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000']], 
           "1010": [['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000']], 
           "1011": [['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000']],
           "1100": [['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000']], 
           "1101": [['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000']], 
           "1110": [['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000']], 
           "1111": [['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000'], ['00000000']]}

################################## FUNCTIONS ##################################


def toBinary(number, zeros):
    binary = bin(number)
    resBinary = binary[2:]
    # print(resBinary)
    if(len(resBinary) < zeros):
        n = zeros - len(resBinary)
        cont = 0
        res = ''
        while(cont < n):
            res += '0'
            cont += 1

        res += resBinary
        # print(res)
        return res
    elif(len(resBinary) > zeros):
        n = len(resBinary)
        indicate = n - zeros

        cont = 0
        res = ''
        while(cont < n):
            if(cont >= indicate):

                res += resBinary[cont]

            cont += 1

        # print(res)
        return res
    else:
        # print(resBinary)
        return resBinary


def toDecimal(number):
    res = '0b' + number
    return int(res, 2)


def circularMoveRight(srcA, srcB):
    cont = 0
    res = ''
    while(cont < srcB):
        res = srcA[-1] + srcA[:-1]
        cont += 1

    return res


def circularMoveLeft(srcA, srcB):
    cont = 0
    res = ''
    while(cont < srcB):
        res = srcA[1:] + srcA[0]
        cont += 1

    return res


class Clock:

    def start(self):
        global clock
        print("All")
        flag = True

        while(flag):
            if(clock == 0):
                clock = 1
            elif(clock == 1):
                clock = 0
            time.sleep(1)
            print("clock: " + str(clock))

################################## OTHER MODULES ##################################


class ALU:
    def __init__(self):
        self.res = ''
    def process8Bits(self, srcAE, srcBE, ALUControlE):
        # print("A ", srcAE)
        # print("B ", srcBE)
        if(ALUControlE == '0100'):
            A = toDecimal(srcAE)
            B = toDecimal(srcBE)
            temp = A + B
            bi = toBinary(temp, 32)
            self.res = bi[24:]
            # print("PROCESS 8 BITS ", self.res)
        elif(ALUControlE == '0010'):
            A = toDecimal(srcAE)
            B = toDecimal(srcBE)
            temp = A - B
            bi = toBinary(temp, 32)
            self.res = bi[24:]
            # print("PROCESS 8 BITS ", self.res)
        elif(ALUControlE == '0001'):
            A = toDecimal(srcAE)
            B = toDecimal(srcBE)
            temp = A ^ B
            bi = toBinary(temp, 32)
            self.res = bi[24:]
            # print("PROCESS 8 BITS ", self.res)
        elif(ALUControlE == '1000'):
            self.res = circularMoveRight(srcAE, toDecimal(srcBE))
            # print("PROCESS 8 BITS ", self.res)
        elif(ALUControlE == '1001'):
            self.res = circularMoveLeft(srcAE, toDecimal(srcBE))
            # print("PROCESS 8 BITS ", self.res)

    def processRegisterImm(self, srcAE, srcBE, ALUControlE):
        if(ALUControlE == '0100'):
            print("SRCA ", srcAE)
            print("SRCB ", srcBE)
            Abin = srcAE[0][0] + srcAE[1][0] + srcAE[2][0] + srcAE[3][0]
            A = toDecimal(Abin)
            B = toDecimal(srcBE)
            temp = A + B
            print("ESTO ES DE LA ALU ADD CON REG IMM", temp)
            bi = toBinary(temp, 32)
            self.res = [[bi[0:8]] , [bi[8:16]] , [bi[16:24]] , [bi[24:]]]
            # print("REGIMM ", self.res)
        elif(ALUControlE == '0010'):
            Abin = srcAE[0][0] + srcAE[1][0] + srcAE[2][0] + srcAE[3][0]
            A = toDecimal(Abin)
            B = toDecimal(srcBE)
            temp = A - B
            bi = toBinary(temp, 32)
            self.res = [[bi[0:8]] , [bi[8:16]] , [bi[16:24]] , [bi[24:]]]
            # print("REGIMM ", self.res)
    def processRegisterRegister(self, srcAE, srcBE, ALUControlE):
        if(ALUControlE == '0100'):
            Abin = srcAE[0][0] + srcAE[1][0] + srcAE[2][0] + srcAE[3][0]
            Bbin = srcBE[0][0] + srcBE[1][0] + srcBE[2][0] + srcBE[3][0]
            A = toDecimal(Abin)
            B = toDecimal(Bbin)
            temp = A + B
            bi = toBinary(temp, 32)
            self.res = [[bi[0:8]] , [bi[8:16]] , [bi[16:24]] , [bi[24:]]]
            # print("REGREG ", self.res)
        elif(ALUControlE == '0010'):
            Abin = srcAE[0][0] + srcAE[1][0] + srcAE[2][0] + srcAE[3][0]
            Bbin = srcBE[0][0] + srcBE[1][0] + srcBE[2][0] + srcBE[3][0]
            A = toDecimal(Abin)
            B = toDecimal(Bbin)
            temp = A - B
            bi = toBinary(temp, 32)
            self.res = [[bi[0:8]] , [bi[8:16]] , [bi[16:24]] , [bi[24:]]]
            # print("REGIMM ", self.res)



class pipeFD:
    def __init__(self):
        self.inst = -1

    def start(self):
        global clock, INSTD, INSTF
        while(True):
            if(clock):
                if(self.inst != -1):
                    INSTD = self.inst
                print("INSTD IS " + str(INSTD))
                time.sleep(1)
            else:
                print("INSTF IS " + str(INSTF))
                self.inst = INSTF
                time.sleep(1)

    def noClock(self):
        global clock, INSTD, INSTF
        if(clock == 1):
            if(self.inst != -1):
                INSTD = self.inst
            print("INSTD IS " + INSTD)
            # print("PIPE FD CLOCK")
        else:
            print("INSTF IS " + INSTF)
            self.inst = INSTF
            # print("NOT PIPE FD CLOCK")


class pipeDE:
    def __init__(self):
        self.immediateNeed = ''
        self.vectorsNeed = ''
        self.op = ''
        self.cmd = ''
        self.l = ''
        self.rd1 = ''
        self.rd2 = '' 
        self.rdv1 = ''
        self.rdv2 = ''
        self.imm = ''
        self.rd = ''
        
        

    def start(self):
        global clock, IMMEDIATE_NEED, VECTORS_NEED, OP, CMD, L, RD1, RD2, RDV1, RDV2, RD, IMMEDIATE
        global IMMEDIATE_NEED_E, VECTORS_NEED_E, OP_E, CMD_E, L_E, RD1_E, RD2_E, RDV1_E, RDV2_E, RD_E, IMMEDIATE_E
        while(True):
            if(clock):
                if(self.cmd != ''):
                    IMMEDIATE_NEED_E = self.immediateNeed
                    VECTORS_NEED_E = self.vectorsNeed
                    OP_E = self.op
                    CMD_E = self.cmd
                    L_E = self.l
                    RD1_E = self.rd1
                    RD2_E = self.rd2
                    RDV1_E = self.rdv1
                    RDV2_E = self.rdv2
                    RD_E=  self.rd
                    IMMEDIATE_E = self.imm
                print("PIPE DE ", IMMEDIATE_NEED_E, VECTORS_NEED_E, OP_E, CMD_E, L_E, RD1_E, RD2_E, RDV1_E, RDV2_E, RD_E, IMMEDIATE_E)
                time.sleep(1)
            else:
                if(CMD != ''):
                    self.immediateNeed = IMMEDIATE_NEED
                    self.vectorsNeed = VECTORS_NEED
                    self.op = OP
                    self.cmd = CMD 
                    self.l = L
                    self.rd1 = RD1
                    self.rd2 = RD2
                    self.rdv1 = RDV1
                    self.rdv2 = RDV2
                    self.rd = RD
                    self.imm = IMMEDIATE
                # print("LOAD DECODE", self.l)
                print("NOT PIPE DE ", self.immediateNeed, self.vectorsNeed, self.op, self.cmd, self.l, self.rd1, self.rd2, self.rdv1, self.rdv2, self.rd, self.imm)
                time.sleep(1)

    def noClock(self):
        global clock, IMMEDIATE_NEED, VECTORS_NEED, OP, CMD, L, RD1, RD2, RDV1, RDV2, RD, IMMEDIATE
        global IMMEDIATE_NEED_E, VECTORS_NEED_E, OP_E, CMD_E, L_E, RD1_E, RD2_E, RDV1_E, RDV2_E, RD_E, IMMEDIATE_E
        if(clock == 1):
            if(self.cmd != ''):
                IMMEDIATE_NEED_E = self.immediateNeed
                VECTORS_NEED_E = self.vectorsNeed
                OP_E = self.op
                CMD_E = self.cmd
                L_E = self.l
                RD1_E = self.rd1
                RD2_E = self.rd2
                RDV1_E = self.rdv1
                RDV2_E = self.rdv2
                RD_E=  self.rd
                IMMEDIATE_E = self.imm
            # print("LOAD DECODE", L_E)
            print("PIPE DE ", IMMEDIATE_NEED_E, VECTORS_NEED_E, OP_E, CMD_E, L_E, RD1_E, RD2_E, RDV1_E, RDV2_E, RD_E, IMMEDIATE_E)
        else:
            if(CMD != ''):
                self.immediateNeed = IMMEDIATE_NEED
                self.vectorsNeed = VECTORS_NEED
                self.op = OP
                self.cmd = CMD 
                self.l = L
                self.rd1 = RD1
                self.rd2 = RD2
                self.rdv1 = RDV1
                self.rdv2 = RDV2
                self.rd = RD
                self.imm = IMMEDIATE
            # print("LOAD DECODE", self.l)
            print("NOT PIPE DE ", self.immediateNeed, self.vectorsNeed, self.op, self.cmd, self.l, self.rd1, self.rd2, self.rdv1, self.rdv2, self.rd, self.imm)
            # print("RD1 ", self.rd1)
            # print("RD2 ", self.rd2)
            # print("RDV1 ", self.rdv1)
            # print("RDV2 ", self.rdv2)
            # print("RD ", self.rd)



class pipeEM:
    def __init__(self):
        self.aluresultm = ''
        self.writedatam = ''
        self.wa3m = ''
        self.opm = ''
        self.cmdm = ''
        self.lm = ''
        self.immediateNeedM = ''
        self.vectorsNeedM = ''
        self.rd1m = ''
        self.rd2m = ''
        self.rdv1m = ''
        self.rdv2m = ''
        self.readm = ''

    def start(self):
        global clock, ALURESULTE, WRITEDATAE, WA3E, OPE, CMDE, LE, IMMEDIATE_NEEDE, VECTORS_NEEDE, RD1E, RD2E, RDV1E, RDV2E, READE
        global ALURESULT_M, WRITEDATA_M, WA3_M, OP_M, CMD_M, L_M, IMMEDIATE_NEED_M, VECTORS_NEED_M, IMMEDIATE_M, READ_M
        while(True):
            if(clock):
                if(CMDE != ''):
                    ALURESULT_M = self.aluresultm
                    WRITEDATA_M = self.writedatam
                    WA3_M = self.wa3m
                    OP_M = self.opm
                    CMD_M = self.cmdm
                    L_M = self.lm
                    IMMEDIATE_NEED_M = self.immediateNeedM
                    VECTORS_NEED_M = self.vectorsNeedM
                    READ_M = self.readm
                # print("LOAD REQUIRED ", L_M)
                # print("LOAD REQUIRED ", IMMEDIATE_NEED_M)
                print()
                print("############ PIPE EM ############")
                print("ALURESULT_M ", ALURESULT_M)
                print("WRITEDATA_M ", WRITEDATA_M)
                print("WA3_M ", WA3_M)
                print("IMMEDIATENEEDM ", IMMEDIATE_NEED_M)
                print("VECTORSNEED_M ", VECTORS_NEED_M)
                print("OP_M ", OP_M)
                print("CMD_M ", CMD_M)
                print("L_M ", self.lm)
                time.sleep(1)
            else:
                if(CMDE != ''):
                    self.aluresultm = ALURESULTE
                    self.writedatam = WRITEDATAE
                    self.wa3m = WA3E
                    self.opm = OPE
                    self.cmdm = CMDE
                    self.lm = LE
                    self.immediateNeedM = IMMEDIATE_NEEDE
                    self.vectorsNeedM = VECTORS_NEEDE
                    self.readm = READE
                # print("LOAD REQUIRED ", self.lm)
                # print("LOAD REQUIRED ", self.immediateNeedM)
                print()
                print("############ NO PIPE EM ############")
                print("ALURESULTM ", self.aluresultm)
                print("WRITEDATAM ", self.writedatam)
                print("WA3M ", self.wa3m)
                print("IMMEDIATENEEDM ", self.immediateNeedM)
                print("VECTORSNEEDM ", self.vectorsNeedM)
                print("OPM ", self.opm)
                print("CMDM ", self.cmdm)
                print("LM ", self.lm)
                time.sleep(1)

    def noClock(self):
        global clock, ALURESULTE, WRITEDATAE, WA3E, OPE, CMDE, LE, IMMEDIATE_NEEDE, VECTORS_NEEDE, RD1E, RD2E, RDV1E, RDV2E, READE
        global ALURESULT_M, WRITEDATA_M, WA3_M, OP_M, CMD_M, L_M, IMMEDIATE_NEED_M, VECTORS_NEED_M, IMMEDIATE_M, READ_M
        if(clock == 1):
            if(CMDE != ''):
                ALURESULT_M = self.aluresultm
                WRITEDATA_M = self.writedatam
                WA3_M = self.wa3m
                OP_M = self.opm
                CMD_M = self.cmdm
                L_M = self.lm
                IMMEDIATE_NEED_M = self.immediateNeedM
                VECTORS_NEED_M = self.vectorsNeedM
                READ_M = self.readm
            # print("LOAD REQUIRED ", L_M)
            # print("LOAD REQUIRED ", IMMEDIATE_NEED_M)
            print()
            print("############ PIPE EM ############")
            print("ALURESULT_M ", ALURESULT_M)
            print("WRITEDATA_M ", WRITEDATA_M)
            print("WA3_M ", WA3_M)
            print("IMMEDIATENEEDM ", IMMEDIATE_NEED_M)
            print("VECTORSNEED_M ", VECTORS_NEED_M)
            print("OP_M ", OP_M)
            print("CMD_M ", CMD_M)
            print("L_M ", self.lm)
            # print("PIPE EM ", ALURESULT_M, WRITEDATA_M, WA3_M, OP_M, CMD_M, L_M, IMMEDIATE_NEED_M, VECTORS_NEED_M, READ_M)
        else:
            if(CMDE != ''):
                self.aluresultm = ALURESULTE
                self.writedatam = WRITEDATAE
                self.wa3m = WA3E
                self.opm = OPE
                self.cmdm = CMDE
                self.lm = LE
                self.immediateNeedM = IMMEDIATE_NEEDE
                self.vectorsNeedM = VECTORS_NEEDE
                self.readm = READE
            # print("LOAD REQUIRED ", self.lm)
            # print("LOAD REQUIRED ", self.immediateNeedM)
            print()
            print("############ NO PIPE EM ############")
            print("ALURESULTM ", self.aluresultm)
            print("WRITEDATAM ", self.writedatam)
            print("WA3M ", self.wa3m)
            print("IMMEDIATENEEDM ", self.immediateNeedM)
            print("VECTORSNEEDM ", self.vectorsNeedM)
            print("OPM ", self.opm)
            print("CMDM ", self.cmdm)
            print("LM ", self.lm)
            # print("NOT PIPE EM", self.aluresultm, self.writedatam, self.wa3m, self.opm, self.cmdm, self.lm, self.immediateNeedM, self.vectorsNeedM)


class pipeMW:
    def __init__(self):
        self.aluresultw = ''
        self.wa3w = ''
        self.writedataw = ''
        self.immediateNeedw = ''
        self.vectorsNeedw = ''
        self.opw = ''
        self.cmdw = ''
        self.lw = ''


    def start(self):
        global clock, ALURESULTM, WRITEDATAM, WA3M, IMMEDIATE_NEEDM, VECTORS_NEEDM, OPM, CMDM, LM, RD1M, RD2M, RDV1M, RDV2M, RDM, IMMEDIATEM, READM
        global ALURESULT_W, WA3_W, IMMEDIATE_NEED_W, VECTORS_NEED_W, OP_W, CMD_W, L_W
        while(True):
            if(clock):
                if(self.cmdw != ''):
                    ALURESULT_W = self.aluresultw
                    WA3_W = self.wa3w
                    IMMEDIATE_NEED_W = self.immediateNeedw
                    VECTORS_NEED_W = self.vectorsNeedw
                    OP_W = self.opw
                    CMD_W = self.cmdw
                    L_W = self.lw
                print()
                print("############ PIPE MW ############")
                print("ALURESULT_W ", ALURESULT_W)
                print("WA3_W ", WA3_W)
                print("IMMEDIATENEED_W ", IMMEDIATE_NEED_W)
                print("VECTORSNEED_W ", VECTORS_NEED_W)
                print("OP_W ", OP_W)
                print("CMD_W ", CMD_W)
                print("L_W ", L_W)
                time.sleep(1)
            else:
                if(CMDM != ''):
                    self.aluresultw = ALURESULTM
                    self.wa3w = WA3M
                    self.immediateNeedw = IMMEDIATE_NEEDM
                    self.vectorsNeedw = VECTORS_NEEDM
                    self.opw = OPM
                    self.cmdw = CMDM
                    self.lw = LM

                print()
                print("############ NO PIPE MW ############")
                print("ALURESULTW ", self.aluresultw)
                print("WA3W ", self.wa3w)
                print("IMMEDIATENEEDW ", self.immediateNeedw)
                print("VECTORSNEEDW ", self.vectorsNeedw)
                print("OPW ", self.opw)
                print("CMDW ", self.cmdw)
                print("LW ", self.lw)
                time.sleep(1)

    def noClock(self):
        global clock, ALURESULTM, WRITEDATAM, WA3M, IMMEDIATE_NEEDM, VECTORS_NEEDM, OPM, CMDM, LM, RD1M, RD2M, RDV1M, RDV2M, RDM, IMMEDIATEM, READM
        global ALURESULT_W, WA3_W, IMMEDIATE_NEED_W, VECTORS_NEED_W, OP_W, CMD_W, L_W
        if(clock == 1):
            if(self.cmdw != ''):
                ALURESULT_W = self.aluresultw
                WA3_W = self.wa3w
                IMMEDIATE_NEED_W = self.immediateNeedw
                VECTORS_NEED_W = self.vectorsNeedw
                OP_W = self.opw
                CMD_W = self.cmdw
                L_W = self.lw
            print()
            print("############ PIPE MW ############")
            print("ALURESULT_W ", ALURESULT_W)
            print("WA3_W ", WA3_W)
            print("IMMEDIATENEED_W ", IMMEDIATE_NEED_W)
            print("VECTORSNEED_W ", VECTORS_NEED_W)
            print("OP_W ", OP_W)
            print("CMD_W ", CMD_W)
            print("L_W ", L_W)
            # print("PIPE MW CLOCK")
        else:
            if(CMDM != ''):
                self.aluresultw = ALURESULTM
                self.wa3w = WA3M
                self.immediateNeedw = IMMEDIATE_NEEDM
                self.vectorsNeedw = VECTORS_NEEDM
                self.opw = OPM
                self.cmdw = CMDM
                self.lw = LM

            print()
            print("############ NO PIPE MW ############")
            print("ALURESULTW ", self.aluresultw)
            print("WA3W ", self.wa3w)
            print("IMMEDIATENEEDW ", self.immediateNeedw)
            print("VECTORSNEEDW ", self.vectorsNeedw)
            print("OPW ", self.opw)
            print("CMDW ", self.cmdw)
            print("LW ", self.lw)
            # print("NOT PIPE MW CLOCK")


class registerPC:
    def __init__(self, pc):
        self.pc = pc

    def noClock(self):
        global clock, PC, PCF
        if(clock == 1):
            self.pc = PC
            PC = toBinary(toDecimal(self.pc) + 1, 32)
            print()
            print("############ REGISTER PC ############")
            print("PCF " + PCF)
            # print("REGISTER PC CLOCK")
        else:

            PCF = PC
            print()
            print("############ NO REGISTER PC ############")
            print("PCF " + PCF)
            # print("NOT REGISTER PC CLOCK")


################################## FETCH ##################################
class Fetch:
    def __init__(self):
        self.A = -1
        self.RD = -1
        self.registerPC = registerPC(0)
        self.lenInstructionMemory = 0

    def start(self):
        global clock, PCF, INSTF, INSTRUCTION_MEMORY
        while(True):
            if(clock):
                self.registerPC.noClock()
                self.A = PCF
                print("A " + self.A)
                self.RD = INSTRUCTION_MEMORY[toDecimal(self.A)]
                print("INSTRUCTION " + str(self.RD))
                # print("FETCH CLOCK")
                time.sleep(1)
            else:
                self.registerPC.noClock()
                INSTF = self.RD
                print("WRITE INSTF " + str(INSTF))
                time.sleep(1)

    def startInstructionMemory(self):
        global INSTRUCTION_MEMORY, INSTRUCTION_MEMORY_SIZE
        f = open("../compiler/codeBin.rs", "r")

        content = f.read()

        INSTRUCTION_MEMORY = content.split("\n")

        INSTRUCTION_MEMORY = INSTRUCTION_MEMORY[:len(INSTRUCTION_MEMORY)-1]

        print(INSTRUCTION_MEMORY)

        # self.lenInstructionMemory = len(INSTRUCTION_MEMORY)
        # INSTRUCTION_MEMORY = self.lenInstructionMemory

    def noClock(self):
        global clock, PCF, INSTF, INSTRUCTION_MEMORY
        if(clock == 1):
            self.registerPC.noClock()
            self.A = PCF
            print("A " + self.A)
            self.RD = INSTRUCTION_MEMORY[toDecimal(self.A)]
            print("INSTRUCTION " + self.RD)
            # print("FETCH CLOCK")

        else:
            self.registerPC.noClock()
            INSTF = self.RD
            print("WRITE INSTF " + INSTF)

            # print("NOT FETCH CLOCK")


################################## DECODE ##################################

class RegisterFile:
    def __init__(self, A1 , A2, A3, WE3, WD3):
        self.A1 = A1
        self.A2 = A2
        self.A3 = A3
        self.WE3 = WE3
        self.WD3 = WD3

    def noClock(self, a1, a2, a3, we3, wd3):
        global clock, RD1, RD2, REGISTERS

        
        if(clock == 1):
            
            self.A1 = a1
            self.A2 = a2
            # print("A1 A2 ", self.A1 , self.A2)


        else:
            print("WE3 ", we3)
            if(we3 == 1):
                print("MAMAMAMAMAMAMAMAMAMAMAMAMMAMAMAMAMAMAMAMAAMMAMAMAMAMA")
                REGISTERS[a3] = wd3
                print("RESULT OF THE REGISTER ", REGISTERS[a3])
            else:
                if(self.A2 == ''):
                    RD1 = REGISTERS[self.A1]
                    RD2 = ''
                elif(self.A1 == ''):
                    RD1 = ''
                    RD2 = REGISTERS[self.A2]
                else:
                    RD1 = REGISTERS[self.A1]
                    RD2 = REGISTERS[self.A2]
            
            # print("RD1 RD2 ",RD1, RD2)

            

registerFile = RegisterFile('','','','','')

class VectorsFile:
    def __init__(self, A1 , A2, A3, WE3, WD3):
        self.A1 = A1
        self.A2 = A2
        self.A3 = A3
        self.WE3 = WE3
        self.WD3 = WD3
        

    def noClock(self, a1, a2, a3, we3, wd3):
        global clock, RDV1, RDV2, VECTORS
        if(clock == 1):
            self.A1 = a1
            self.A2 = a2
            # print("AV1 AV2 ", self.A1 , self.A2)

        else:
            if(we3 == 1):
                VECTORS[a3] = wd3
                print("RESULT OF THE VECTOR ", VECTORS[a3])
            else:
                if(self.A2 == ''):
                    RDV1 = VECTORS[self.A1]
                    RDV2 = ''
                elif(self.A1 == ''):
                    RDV1 = ''
                    RDV2 = VECTORS[self.A2]
                else:
                    RDV1 = VECTORS[self.A1]
                    RDV2 = VECTORS[self.A2]
            # print("RDV1 RDV2 ", RDV1, RDV2)
        
vectorsFile = VectorsFile('', '', '', '', '')

class Decode:
    def __init__(self):
        self.cond = ''
        self.op = ''
        self.i = ''
        self.v = ''
        self.cmd = ''
        self.rn = ''
        self.rd = ''
        self.src = ''
        self.p = ''
        self.u = ''
        self.w = ''
        self.l = ''
        self.imm = ''
        self.rd1 = ''
        self.rd2 = ''
        self.rdv1 = ''
        self.rdv2 = ''
        self.rdpipe = ''

    def start(self):
        global clock, INSTD, RD1, RD2, RDV1, RDV2, RD, registerFile, vectorsFile, OP, L, IMMEDIATE_NEED, VECTORS_NEED, IMMEDIATE, CMD
        while(True):
            if(clock):
                if(INSTD != ''):
                    self.cond = INSTF[0:4]
                    self.op = INSTF[4:6]
                    
                    if(self.op == '00'):
                        self.i = INSTF[6]
                        self.v = INSTF[7]
                        self.cmd = INSTF[8:12]
                        self.rn = INSTF[12:16]
                        self.rd = INSTF[16:20]
                        self.src = INSTF[20:]

                        if(self.v == '0'):
                            if(self.i == '0'):
                                registerFile.noClock(self.rn, self.src[8:], '', '', '')
                                self.rdpipe = self.rd
                            elif(self.i == '1'):
                                registerFile.noClock(self.rn, '', '', '', '')
                                self.imm = self.src
                                self.rdpipe = self.rd
                                
                        elif(self.v == '1'):
                            if(self.i == '0'):
                                vectorsFile.noClock(self.rn, self.src[8:], '', '', '')
                                self.rdpipe = self.rd
                            elif(self.i == '1'):
                                vectorsFile.noClock(self.rn, '', '', '', '')
                                self.imm = self.src
                                self.rdpipe = self.rd
                    elif(self.op == '01'):
                        self.i = INSTF[6]
                        self.p = INSTF[7]
                        self.u = INSTF[8]
                        self.v = INSTF[9]
                        self.w = INSTF[10]
                        self.l = INSTF[11]
                        self.rn = INSTF[12:16]
                        self.rd = INSTF[16:20]
                        self.src = INSTF[20:]

                        if(self.v == '0'):
                            if(self.l == '0'): # STR
                                registerFile.noClock(self.rn, self.rd, '' , '', '')
                                self.imm = self.src
                            elif(self.l == '1'): # LDR
                                registerFile.noClock('', self.rn, '', '', '')
                                self.rdpipe = self.rd
                                self.imm = self.src
                        elif(self.v == '1'):
                            if(self.l == '0'): # STRV
                                registerFile.noClock('', self.rn, '', '', '')
                                vectorsFile.noClock(self.rd,  '', '', '', '')
                                self.imm = self.src
                            elif(self.l == '1'): # LDRV
                                registerFile.noClock('', self.rn, '','','')
                                self.rdpipe = self.rd
                                self.imm = self.src
                print()
                print("############ DECODE ############")
                print("OP ", self.op)
                print("CMD ", self.cmd)
                print("I ", self.i)
                print("V ", self.v)
                print("Rn ", self.rn)
                print("Rd ", self.rd)
                print("Src ", self.src)
                print("DECODE CLOCK")
                time.sleep(1)
            else:
                if(self.op == '00'):
                    if(self.v == '0'):
                        if(self.i == '0'):
                            registerFile.noClock('','', '', '', '')
                            RD = self.rdpipe 
                            IMMEDIATE_NEED = self.i
                            VECTORS_NEED = self.v
                            IMMEDIATE = self.imm 
                            CMD = self.cmd
                            OP = self.op
                        elif(self.i == '1'):
                            registerFile.noClock('', '', '', '', '')
                            IMMEDIATE = self.imm 
                            RD = self.rdpipe
                            IMMEDIATE_NEED = self.i
                            VECTORS_NEED = self.v
                            CMD = self.cmd
                            OP = self.op
                    elif(self.v == '1'):
                        if(self.i == '0'):
                            vectorsFile.noClock('','', '', '', '')
                            RD = self.rdpipe 
                            IMMEDIATE_NEED = self.i
                            VECTORS_NEED = self.v
                            IMMEDIATE = self.imm 
                            CMD = self.cmd
                            OP = self.op
                        elif(self.i == '1'):
                            vectorsFile.noClock('', '', '', '', '')
                            IMMEDIATE = self.imm 
                            RD = self.rdpipe
                            IMMEDIATE_NEED = self.i
                            VECTORS_NEED = self.v
                            CMD = self.cmd
                            OP = self.op
                elif(self.op == '01'):
                    if(self.v == '0'):
                        if(self.l == '0'): # STR
                            registerFile.noClock('','','' ,'','')
                            IMMEDIATE = self.imm
                            IMMEDIATE_NEED = self.i
                            VECTORS_NEED = self.v
                            OP = self.op
                            L = self.l
                        elif(self.l == '1'): # LDR
                            registerFile.noClock('','','', '', '')
                            RD = self.rdpipe
                            IMMEDIATE = self.imm
                            IMMEDIATE_NEED = self.i
                            VECTORS_NEED = self.v
                            OP = self.op
                            L = self.l
                    elif(self.v == '1'):
                        if(self.l == '0'): # STRV
                            registerFile.noClock('','','','','')
                            vectorsFile.noClock('','','','','')
                            IMMEDIATE = self.imm
                            IMMEDIATE_NEED = self.i
                            VECTORS_NEED = self.v
                            OP = self.op
                            L = self.l
                        elif(self.l == '1'): # LDRV
                            registerFile.noClock('','', '','','')
                            RD = self.rdpipe
                            IMMEDIATE = self.imm
                            IMMEDIATE_NEED = self.i
                            VECTORS_NEED = self.v
                            OP = self.op
                            L = self.l

                print()
                print("############ NO DECODE ############")
                print("IMMEDIATENEED ", IMMEDIATE_NEED)
                print("VECTORSNEED ", VECTORS_NEED)
                print("OP ", OP)
                print("CMD ", CMD)
                print("L ", L)
                print("RD1 ", RD1)
                print("RD2 ", RD2)
                print("RDV1 ", RDV1)
                print("RDV2 ", RDV2)
                print("RD ", RD)
                print("IMM ", IMMEDIATE)
                time.sleep(1)

    def noClock(self):
        global clock, INSTD, RD1, RD2, RDV1, RDV2, RD, registerFile, vectorsFile, OP, L, IMMEDIATE_NEED, VECTORS_NEED, IMMEDIATE, CMD
        if(clock == 1):
            if(INSTD != ''):
                self.cond = INSTF[0:4]
                self.op = INSTF[4:6]
                
                if(self.op == '00'):
                    self.i = INSTF[6]
                    self.v = INSTF[7]
                    self.cmd = INSTF[8:12]
                    self.rn = INSTF[12:16]
                    self.rd = INSTF[16:20]
                    self.src = INSTF[20:]

                    if(self.v == '0'):
                        if(self.i == '0'):
                            registerFile.noClock(self.rn, self.src[8:], '', '', '')
                            self.rdpipe = self.rd
                        elif(self.i == '1'):
                            registerFile.noClock(self.rn, '', '', '', '')
                            self.imm = self.src
                            self.rdpipe = self.rd
                            
                    elif(self.v == '1'):
                        if(self.i == '0'):
                            vectorsFile.noClock(self.rn, self.src[8:], '', '', '')
                            self.rdpipe = self.rd
                        elif(self.i == '1'):
                            vectorsFile.noClock(self.rn, '', '', '', '')
                            self.imm = self.src
                            self.rdpipe = self.rd
                elif(self.op == '01'):
                    self.i = INSTF[6]
                    self.p = INSTF[7]
                    self.u = INSTF[8]
                    self.v = INSTF[9]
                    self.w = INSTF[10]
                    self.l = INSTF[11]
                    self.rn = INSTF[12:16]
                    self.rd = INSTF[16:20]
                    self.src = INSTF[20:]

                    if(self.v == '0'):
                        if(self.l == '0'): # STR
                            registerFile.noClock(self.rn, self.rd, '' , '', '')
                            self.imm = self.src
                        elif(self.l == '1'): # LDR
                            registerFile.noClock('', self.rn, '', '', '')
                            self.rdpipe = self.rd
                            self.imm = self.src
                    elif(self.v == '1'):
                        if(self.l == '0'): # STRV
                            registerFile.noClock('', self.rn, '', '', '')
                            vectorsFile.noClock(self.rd,  '', '', '', '')
                            self.imm = self.src
                        elif(self.l == '1'): # LDRV
                            registerFile.noClock('', self.rn, '','','')
                            self.rdpipe = self.rd
                            self.imm = self.src
                print()
                print("############ DECODE ############")
                print("OP ", self.op)
                print("CMD ", self.cmd)
                print("I ", self.i)
                print("V ", self.v)
                print("Rn ", self.rn)
                print("Rd ", self.rd)
                print("Src ", self.src)
                # print(self.cond, self.op, self.i, self.v, self.cmd, self.rn, self.rd, self.src)
            # print("DECODE CLOCK")
        else:
            if(self.op == '00'):
                if(self.v == '0'):
                    if(self.i == '0'):
                        registerFile.noClock('','', '', '', '')
                        RD = self.rdpipe 
                        IMMEDIATE_NEED = self.i
                        VECTORS_NEED = self.v
                        IMMEDIATE = self.imm 
                        CMD = self.cmd
                        OP = self.op
                    elif(self.i == '1'):
                        registerFile.noClock('', '', '', '', '')
                        IMMEDIATE = self.imm 
                        RD = self.rdpipe
                        IMMEDIATE_NEED = self.i
                        VECTORS_NEED = self.v
                        CMD = self.cmd
                        OP = self.op
                elif(self.v == '1'):
                    if(self.i == '0'):
                        vectorsFile.noClock('','', '', '', '')
                        RD = self.rdpipe 
                        IMMEDIATE_NEED = self.i
                        VECTORS_NEED = self.v
                        IMMEDIATE = self.imm 
                        CMD = self.cmd
                        OP = self.op
                    elif(self.i == '1'):
                        vectorsFile.noClock('', '', '', '', '')
                        IMMEDIATE = self.imm 
                        RD = self.rdpipe
                        IMMEDIATE_NEED = self.i
                        VECTORS_NEED = self.v
                        CMD = self.cmd
                        OP = self.op
            elif(self.op == '01'):
                if(self.v == '0'):
                    if(self.l == '0'): # STR
                        registerFile.noClock('','','' ,'','')
                        IMMEDIATE = self.imm
                        IMMEDIATE_NEED = self.i
                        VECTORS_NEED = self.v
                        OP = self.op
                        L = self.l
                    elif(self.l == '1'): # LDR
                        registerFile.noClock('','','', '', '')
                        RD = self.rdpipe
                        IMMEDIATE = self.imm
                        IMMEDIATE_NEED = self.i
                        VECTORS_NEED = self.v
                        OP = self.op
                        L = self.l
                elif(self.v == '1'):
                    if(self.l == '0'): # STRV
                        registerFile.noClock('','','','','')
                        vectorsFile.noClock('','','','','')
                        IMMEDIATE = self.imm
                        IMMEDIATE_NEED = self.i
                        VECTORS_NEED = self.v
                        OP = self.op
                        L = self.l
                    elif(self.l == '1'): # LDRV
                        registerFile.noClock('','', '','','')
                        RD = self.rdpipe
                        IMMEDIATE = self.imm
                        IMMEDIATE_NEED = self.i
                        VECTORS_NEED = self.v
                        OP = self.op
                        L = self.l

            print()
            print("############ NO DECODE ############")
            print("IMMEDIATENEED ", IMMEDIATE_NEED)
            print("VECTORSNEED ", VECTORS_NEED)
            print("OP ", OP)
            print("CMD ", CMD)
            print("L ", L)
            print("RD1 ", RD1)
            print("RD2 ", RD2)
            print("RDV1 ", RDV1)
            print("RDV2 ", RDV2)
            print("RD ", RD)
            print("IMM ", IMMEDIATE)
            # print(IMMEDIATE_NEED, VECTORS_NEED, OP, CMD, L, RD1, RD2, RDV1, RDV2, RD, IMMEDIATE)
            
            # print("NOT DECODE CLOCK")


################################## EXECUTE ##################################
class Execute:
    def __init__(self):
        self.immediateNeedE = ''
        self.vectorsNeedE = ''
        self.opE = ''
        self.cmdE = ''
        self.lE = ''
        self.rd1E = ''
        self.rd2E = ''
        self.rdv1E = ''
        self.rdv2E = ''
        self.rdE = ''
        self.immE = ''
        self.alu1 = ALU()
        self.alu2 = ALU()
        self.alu3 = ALU()
        self.alu4 = ALU()
        self.alu5 = ALU()
        self.alu6 = ALU()
        self.alu7 = ALU()
        self.alu8 = ALU()

    def start(self):
        global clock, IMMEDIATE_NEED_E, VECTORS_NEED_E, OP_E, CMD_E, L_E, RD1_E, RD2_E, RDV1_E, RDV2_E, RD_E, IMMEDIATE_E
        global ALURESULTE, WRITEDATAE, WA3E, OPE, CMDE, LE, IMMEDIATE_NEEDE, VECTORS_NEEDE, RD1E, RD2E, RDV1E, RDV2E, READE
        while(True):
            if(clock):
                if(CMD_E != ''):
                    self.immediateNeedE = IMMEDIATE_NEED_E
                    self.vectorsNeedE = VECTORS_NEED_E
                    self.opE = OP_E
                    self.cmdE = CMD_E
                    self.lE = L_E
                    self.rd1E = RD1_E
                    self.rd2E = RD2_E
                    self.rdv1E = RDV1_E
                    self.rdv2E = RDV2_E
                    self.rdE = RD_E
                    self.immE = IMMEDIATE_E

                    if(self.opE == '00'):
                        if(self.immediateNeedE == '0'):
                            if(self.vectorsNeedE == '0'):
                                self.alu1.processRegisterRegister(self.rd1E, self.rd2E, self.cmdE)
                            elif(self.vectorsNeedE == '1'):
                                self.alu1.process8Bits(self.rdv1E[0][0], self.rdv2E[0][0], self.cmdE)
                                self.alu2.process8Bits(self.rdv1E[1][0], self.rdv2E[1][0], self.cmdE)
                                self.alu3.process8Bits(self.rdv1E[2][0], self.rdv2E[2][0], self.cmdE)
                                self.alu4.process8Bits(self.rdv1E[3][0], self.rdv2E[3][0], self.cmdE)
                                self.alu5.process8Bits(self.rdv1E[4][0], self.rdv2E[4][0], self.cmdE)
                                self.alu6.process8Bits(self.rdv1E[5][0], self.rdv2E[5][0], self.cmdE)
                                self.alu7.process8Bits(self.rdv1E[6][0], self.rdv2E[6][0], self.cmdE)
                                self.alu8.process8Bits(self.rdv1E[7][0], self.rdv2E[7][0], self.cmdE)
                        elif(self.immediateNeedE == '1'):
                            if(self.vectorsNeedE == '0'):
                                print("EXECUTION IMMEDIATE", self.immE)
                                self.alu1.processRegisterImm(self.rd1E, self.immE , self.cmdE)
                            elif(self.vectorsNeedE == '1'):
                                print("EXECUTION IMMEDIATE", self.immE)
                                self.alu1.process8Bits(self.rdv1E[0][0], self.immE[4:], self.cmdE)
                                self.alu2.process8Bits(self.rdv1E[1][0], self.immE[4:], self.cmdE)
                                self.alu3.process8Bits(self.rdv1E[2][0], self.immE[4:], self.cmdE)
                                self.alu4.process8Bits(self.rdv1E[3][0], self.immE[4:], self.cmdE)
                                self.alu5.process8Bits(self.rdv1E[4][0], self.immE[4:], self.cmdE)
                                self.alu6.process8Bits(self.rdv1E[5][0], self.immE[4:], self.cmdE)
                                self.alu7.process8Bits(self.rdv1E[6][0], self.immE[4:], self.cmdE)
                                self.alu8.process8Bits(self.rdv1E[7][0], self.immE[4:], self.cmdE)
                print()
                print("############ EXECUTE ############")
                print("IMMEDIATENEED_M ", self.immediateNeedE)
                print("VECTORSNEED_M ", self.vectorsNeedE)
                print("OP_M ", self.opE)
                print("CMD_M ", self.cmdE)
                print("RD1E ", self.rd1E)
                print("RD2E ", self.rd2E)
                print("RDV1E ", self.rdv1E)
                print("RDV2E ", self.rdv2E)
                print("RDE ", self.rdE)
                print("IMME ", self.immE)
                time.sleep(1)
            else:
                if(self.opE == '00'):
                    if(self.immediateNeedE == '0'):
                        if(self.vectorsNeedE == '0'):
                            ALURESULTE = self.alu1.res
                            WA3E = self.rdE # Rd
                            WRITEDATAE = '' # Rn
                            OPE = self.opE
                            CMDE = self.cmdE
                            LE = self.lE
                            IMMEDIATE_NEEDE = self.immediateNeedE
                            VECTORS_NEEDE = self.vectorsNeedE
                        elif(self.vectorsNeedE == '1'):
                            ALURESULTE = [[self.alu1.res], [self.alu2.res], [self.alu3.res], [self.alu4.res], [self.alu5.res], [self.alu6.res], [self.alu7.res], [self.alu8.res]]
                            WA3E = self.rdE # Rd
                            WRITEDATAE = '' # Rn
                            OPE = self.opE
                            CMDE = self.cmdE
                            LE = self.lE
                            IMMEDIATE_NEEDE = self.immediateNeedE
                            VECTORS_NEEDE = self.vectorsNeedE
                    elif(self.immediateNeedE == '1'):
                        if(self.vectorsNeedE == '0'):
                            ALURESULTE = self.alu1.res
                            WA3E = self.rdE # Rd
                            WRITEDATAE = '' # Rn
                            OPE = self.opE
                            CMDE = self.cmdE
                            LE = self.lE
                            IMMEDIATE_NEEDE = self.immediateNeedE
                            VECTORS_NEEDE = self.vectorsNeedE
                        elif(self.vectorsNeedE == '1'):
                            ALURESULTE = [[self.alu1.res], [self.alu2.res], [self.alu3.res], [self.alu4.res], [self.alu5.res], [self.alu6.res], [self.alu7.res], [self.alu8.res]]
                            WA3E = self.rdE # Rd
                            WRITEDATAE = '' # Rn
                            OPE = self.opE
                            CMDE = self.cmdE
                            LE = self.lE
                            IMMEDIATE_NEEDE = self.immediateNeedE
                            VECTORS_NEEDE = self.vectorsNeedE
                elif(self.opE == '01'):
                    if(self.vectorsNeedE == '0'):
                        if(self.lE == '0'):# STR
                            WRITEDATAE = self.rd1E # Rn
                            ALURESULTE = self.rd2E # Rd
                            OPE = self.opE
                            CMDE = self.cmdE
                            LE = self.lE
                            IMMEDIATE_NEEDE = self.immediateNeedE
                            VECTORS_NEEDE = self.vectorsNeedE
                        elif(self.lE == '1'):# LDR
                            ALURESULTE = self.rd2E
                            READE = ''
                            WA3E = self.rdE
                            OPE = self.opE
                            CMDE = self.cmdE
                            LE = self.lE
                            IMMEDIATE_NEEDE = self.immediateNeedE
                            VECTORS_NEEDE = self.vectorsNeedE
                    elif(self.vectorsNeedE == '1'):
                        if(self.lE == '0'):# STRV
                            WRITEDATAE = self.rd2E
                            ALURESULTE = self.rdv1E
                            OPE = self.opE
                            CMDE = self.cmdE
                            LE = self.lE
                            IMMEDIATE_NEEDE = self.immediateNeedE
                            VECTORS_NEEDE = self.vectorsNeedE
                        elif(self.lE == '1'):# LDRV
                            ALURESULTE = self.rd2E
                            READE = ''
                            WA3E = self.rdE
                            LE = self.lE
                            OPE = self.opE
                            CMDE = self.cmdE
                            IMMEDIATE_NEEDE = self.immediateNeedE
                            VECTORS_NEEDE = self.vectorsNeedE
                print()
                print("############ NO EXECUTE ############")
                print("ALURESULTE ", ALURESULTE)
                print("WA3E ", WA3E)
                print("WRITEDATAE ", WRITEDATAE)
                print("IMMEDIATENEEDE ", IMMEDIATE_NEEDE)
                print("VECTORSNEEDE ", VECTORS_NEEDE)
                print("OPE ", OPE)
                print("CMDE ", CMDE)
                print("LE ", LE)
                time.sleep(1)

    def noClock(self):
        global clock, IMMEDIATE_NEED_E, VECTORS_NEED_E, OP_E, CMD_E, L_E, RD1_E, RD2_E, RDV1_E, RDV2_E, RD_E, IMMEDIATE_E
        global ALURESULTE, WRITEDATAE, WA3E, OPE, CMDE, LE, IMMEDIATE_NEEDE, VECTORS_NEEDE, RD1E, RD2E, RDV1E, RDV2E, READE
        if(clock == 1):
            if(CMD_E != ''):
                self.immediateNeedE = IMMEDIATE_NEED_E
                self.vectorsNeedE = VECTORS_NEED_E
                self.opE = OP_E
                self.cmdE = CMD_E
                self.lE = L_E
                self.rd1E = RD1_E
                self.rd2E = RD2_E
                self.rdv1E = RDV1_E
                self.rdv2E = RDV2_E
                self.rdE = RD_E
                self.immE = IMMEDIATE_E

                if(self.opE == '00'):
                    if(self.immediateNeedE == '0'):
                        if(self.vectorsNeedE == '0'):
                            self.alu1.processRegisterRegister(self.rd1E, self.rd2E, self.cmdE)
                        elif(self.vectorsNeedE == '1'):
                            self.alu1.process8Bits(self.rdv1E[0][0], self.rdv2E[0][0], self.cmdE)
                            self.alu2.process8Bits(self.rdv1E[1][0], self.rdv2E[1][0], self.cmdE)
                            self.alu3.process8Bits(self.rdv1E[2][0], self.rdv2E[2][0], self.cmdE)
                            self.alu4.process8Bits(self.rdv1E[3][0], self.rdv2E[3][0], self.cmdE)
                            self.alu5.process8Bits(self.rdv1E[4][0], self.rdv2E[4][0], self.cmdE)
                            self.alu6.process8Bits(self.rdv1E[5][0], self.rdv2E[5][0], self.cmdE)
                            self.alu7.process8Bits(self.rdv1E[6][0], self.rdv2E[6][0], self.cmdE)
                            self.alu8.process8Bits(self.rdv1E[7][0], self.rdv2E[7][0], self.cmdE)
                    elif(self.immediateNeedE == '1'):
                        if(self.vectorsNeedE == '0'):
                            print("EXECUTION IMMEDIATE", self.immE)
                            self.alu1.processRegisterImm(self.rd1E, self.immE , self.cmdE)
                            
                        elif(self.vectorsNeedE == '1'):
                            print("EXECUTION IMMEDIATE", self.immE)
                            self.alu1.process8Bits(self.rdv1E[0][0], self.immE[4:], self.cmdE)
                            self.alu2.process8Bits(self.rdv1E[1][0], self.immE[4:], self.cmdE)
                            self.alu3.process8Bits(self.rdv1E[2][0], self.immE[4:], self.cmdE)
                            self.alu4.process8Bits(self.rdv1E[3][0], self.immE[4:], self.cmdE)
                            self.alu5.process8Bits(self.rdv1E[4][0], self.immE[4:], self.cmdE)
                            self.alu6.process8Bits(self.rdv1E[5][0], self.immE[4:], self.cmdE)
                            self.alu7.process8Bits(self.rdv1E[6][0], self.immE[4:], self.cmdE)
                            self.alu8.process8Bits(self.rdv1E[7][0], self.immE[4:], self.cmdE)
                
                    


            print()
            print("############ EXECUTE ############")
            print("IMMEDIATENEED_M ", self.immediateNeedE)
            print("VECTORSNEED_M ", self.vectorsNeedE)
            print("OP_M ", self.opE)
            print("CMD_M ", self.cmdE)
            print("RD1E ", self.rd1E)
            print("RD2E ", self.rd2E)
            print("RDV1E ", self.rdv1E)
            print("RDV2E ", self.rdv2E)
            print("RDE ", self.rdE)
            print("IMME ", self.immE)
            

            # print("EXECUTE ", self.immediateNeedE, self.vectorsNeedE, self.opE, self.cmdE, self.lE, self.rd1E, self.rd2E, self.rdv1E, self.rdv2E, self.rdE, self.immE )
        else:
            if(self.opE == '00'):
                if(self.immediateNeedE == '0'):
                    if(self.vectorsNeedE == '0'):
                        ALURESULTE = self.alu1.res
                        WA3E = self.rdE # Rd
                        WRITEDATAE = '' # Rn
                        OPE = self.opE
                        CMDE = self.cmdE
                        LE = self.lE
                        IMMEDIATE_NEEDE = self.immediateNeedE
                        VECTORS_NEEDE = self.vectorsNeedE
                    elif(self.vectorsNeedE == '1'):
                        ALURESULTE = [[self.alu1.res], [self.alu2.res], [self.alu3.res], [self.alu4.res], [self.alu5.res], [self.alu6.res], [self.alu7.res], [self.alu8.res]]
                        WA3E = self.rdE # Rd
                        WRITEDATAE = '' # Rn
                        OPE = self.opE
                        CMDE = self.cmdE
                        LE = self.lE
                        IMMEDIATE_NEEDE = self.immediateNeedE
                        VECTORS_NEEDE = self.vectorsNeedE
                elif(self.immediateNeedE == '1'):
                    if(self.vectorsNeedE == '0'):
                        ALURESULTE = self.alu1.res
                        WA3E = self.rdE # Rd
                        WRITEDATAE = '' # Rn
                        OPE = self.opE
                        CMDE = self.cmdE
                        LE = self.lE
                        IMMEDIATE_NEEDE = self.immediateNeedE
                        VECTORS_NEEDE = self.vectorsNeedE
                    elif(self.vectorsNeedE == '1'):
                        ALURESULTE = [[self.alu1.res], [self.alu2.res], [self.alu3.res], [self.alu4.res], [self.alu5.res], [self.alu6.res], [self.alu7.res], [self.alu8.res]]
                        WA3E = self.rdE # Rd
                        WRITEDATAE = '' # Rn
                        OPE = self.opE
                        CMDE = self.cmdE
                        LE = self.lE
                        IMMEDIATE_NEEDE = self.immediateNeedE
                        VECTORS_NEEDE = self.vectorsNeedE
            elif(self.opE == '01'):
                if(self.vectorsNeedE == '0'):
                    if(self.lE == '0'):# STR
                        WRITEDATAE = self.rd1E # Rn
                        ALURESULTE = self.rd2E # Rd
                        OPE = self.opE
                        CMDE = self.cmdE
                        LE = self.lE
                        IMMEDIATE_NEEDE = self.immediateNeedE
                        VECTORS_NEEDE = self.vectorsNeedE
                    elif(self.lE == '1'):# LDR
                        ALURESULTE = self.rd2E
                        READE = ''
                        WA3E = self.rdE
                        OPE = self.opE
                        CMDE = self.cmdE
                        LE = self.lE
                        IMMEDIATE_NEEDE = self.immediateNeedE
                        VECTORS_NEEDE = self.vectorsNeedE
                elif(self.vectorsNeedE == '1'):
                    if(self.lE == '0'):# STRV
                        WRITEDATAE = self.rd2E
                        ALURESULTE = self.rdv1E
                        OPE = self.opE
                        CMDE = self.cmdE
                        LE = self.lE
                        IMMEDIATE_NEEDE = self.immediateNeedE
                        VECTORS_NEEDE = self.vectorsNeedE
                    elif(self.lE == '1'):# LDRV
                        ALURESULTE = self.rd2E
                        READE = ''
                        WA3E = self.rdE
                        LE = self.lE
                        OPE = self.opE
                        CMDE = self.cmdE
                        IMMEDIATE_NEEDE = self.immediateNeedE
                        VECTORS_NEEDE = self.vectorsNeedE
            print()
            print("############ NO EXECUTE ############")
            print("ALURESULTE ", ALURESULTE)
            print("WA3E ", WA3E)
            print("WRITEDATAE ", WRITEDATAE)
            print("IMMEDIATENEEDE ", IMMEDIATE_NEEDE)
            print("VECTORSNEEDE ", VECTORS_NEEDE)
            print("OPE ", OPE)
            print("CMDE ", CMDE)
            print("LE ", LE)
            # print("NO EXECUTE ", ALURESULTE, WRITEDATAE, WA3E, OPE, CMDE, LE, IMMEDIATE_NEEDE, VECTORS_NEEDE, READE)

            # print("NOT EXECUTE CLOCK")

################################## MEMORY ##################################


class Memory:

    def __init__(self):
        self.readm = ''
        self.wa3m = ''
        self.aluresultm = ''
        self.writedatam = ''
        self.immediateNeedm = ''
        self.vectorsNeedm = ''
        self.opm = ''
        self.cmdm = ''
        self.lm = ''


    def start(self):
        global clock, ALURESULT_M, WRITEDATA_M, WA3_M, IMMEDIATE_NEED_M, VECTORS_NEED_M, OP_M, CMD_M, L_M, RD1_M, RD2_M, RDV1_M, RDV2_M, RD_M, IMMEDIATE_M, READ_M
        global ALURESULTM, WRITEDATAM, WA3M, IMMEDIATE_NEEDM, VECTORS_NEEDM, OPM, CMDM, LM, RD1M, RD2M, RDV1M, RDV2M, RDM, IMMEDIATEM, READM
        global INSTRUCTION_MEMORY, MEMORY_ARRAY
        while(True):
            if(clock):
                if(CMD_M != ''):
                    self.aluresultm = ALURESULT_M
                    self.readm = READ_M
                    self.wa3m = WA3_M
                    self.writedatam = WRITEDATA_M
                    self.immediateNeedm = IMMEDIATE_NEED_M
                    self.vectorsNeedm = VECTORS_NEED_M
                    self.opm = OP_M
                    self.cmdm = CMD_M
                    self.lm = L_M

                print()
                print("############ MEMORY ############")
                print("ALURESULT_M ", self.aluresultm)
                print("WA3_M ", self.wa3m)
                print("WRITEDATA_M ", self.writedatam)
                print("IMMEDIATENEED_M ", self.immediateNeedm)
                print("VECTORSNEED_M ", self.vectorsNeedm)
                print("OP_M ", self.opm)
                print("CMD_M ", self.cmdm)
                print("L_M ", self.lm)
                time.sleep(1)
            else:
                if(self.opm == '00'):
                    if(self.immediateNeedm == '0'):
                        if(self.vectorsNeedm == '0'):
                            ALURESULTM = self.aluresultm
                            WA3M = self.wa3m
                            WRITEDATAM = ''
                            IMMEDIATE_NEEDM = self.immediateNeedm
                            VECTORS_NEEDM = self.vectorsNeedm
                            LM = self.lm
                            OPM = self.opm
                            CMDM = self.cmdm
                        elif(self.vectorsNeedm == '1'):
                            ALURESULTM = self.aluresultm
                            WA3M = self.wa3m
                            WRITEDATAM = ''
                            IMMEDIATE_NEEDM = self.immediateNeedm
                            VECTORS_NEEDM = self.vectorsNeedm
                            LM = self.lm
                            OPM = self.opm
                            CMDM = self.cmdm
                    elif(self.immediateNeedm == '1'):
                        if(self.vectorsNeedm == '0'):
                            ALURESULTM = self.aluresultm
                            WA3M = self.wa3m
                            WRITEDATAM = ''
                            IMMEDIATE_NEEDM = self.immediateNeedm
                            VECTORS_NEEDM = self.vectorsNeedm
                            LM = self.lm
                            OPM = self.opm
                            CMDM = self.cmdm
                        elif(self.vectorsNeedm == '1'):
                            ALURESULTM = self.aluresultm
                            WA3M = self.wa3m
                            WRITEDATAM = ''
                            IMMEDIATE_NEEDM = self.immediateNeedm
                            VECTORS_NEEDM = self.vectorsNeedm
                            LM = self.lm
                            OPM = self.opm
                            CMDM = self.cmdm
                elif(self.opm == '01'):
                    if(self.vectorsNeedm == '0'):
                        if(self.lm == '0'): # STR
                            print("STR WRITEDATA", self.writedatam)
                            data = toDecimal(self.writedatam[0][0] + self.writedatam[1][0] + self.writedatam[2][0] + self.writedatam[3][0])
                            print("DATA", data)
                            print("INSTRUCTION MEMORY ", MEMORY_ARRAY[data])
                            print("ALURESULTM ", self.aluresultm)
                            MEMORY_ARRAY[data] = self.aluresultm
                            ALURESULTM = ''
                            WA3M = ''
                            WRITEDATAM = ''
                            IMMEDIATE_NEEDM = self.immediateNeedm
                            VECTORS_NEEDM = self.vectorsNeedm
                            LM = self.lm
                            OPM = self.opm
                            CMDM = self.cmdm
                        elif(self.lm == '1'): # LDR
                            data = toDecimal(self.aluresultm[0][0] + self.aluresultm[1][0] + self.aluresultm[2][0] + self.aluresultm[3][0])
                            ALURESULTM = MEMORY_ARRAY[data]
                            WRITEDATAM = ''
                            WA3M = self.wa3m
                            IMMEDIATE_NEEDM = self.immediateNeedm
                            VECTORS_NEEDM = self.vectorsNeedm
                            LM = self.lm
                            OPM = self.opm
                            CMDM = self.cmdm
                    elif(self.vectorsNeedm == '1'):
                        if(self.lm == '0'): # STRV
                            data = toDecimal(self.writedatam[0][0] + self.writedatam[1][0] + self.writedatam[2][0] + self.writedatam[3][0])
                            MEMORY_ARRAY[data] = [self.aluresultm[0] , self.aluresultm[1], self.aluresultm[2], self.aluresultm[3]]
                            MEMORY_ARRAY[data + 1] = [self.aluresultm[4] , self.aluresultm[5], self.aluresultm[6], self.aluresultm[7]]
                            ALURESULTM = ''
                            WA3M = ''
                            WRITEDATAM = ''
                            IMMEDIATE_NEEDM = self.immediateNeedm
                            VECTORS_NEEDM = self.vectorsNeedm
                            LM = self.lm
                            OPM = self.opm
                            CMDM = self.cmdm 
                        elif(self.lm == '1'): # LDRV
                            data = toDecimal(self.aluresultm[0][0] + self.aluresultm[1][0] + self.aluresultm[2][0] + self.aluresultm[3][0])
                            aluTemp = MEMORY_ARRAY[data] + MEMORY_ARRAY[data + 1]
                            ALURESULTM = aluTemp
                            WRITEDATAM = ''
                            WA3M = self.wa3m
                            IMMEDIATE_NEEDM = self.immediateNeedm
                            VECTORS_NEEDM = self.vectorsNeedm
                            LM = self.lm
                            OPM = self.opm
                            CMDM = self.cmdm
                print()
                print("############ NO MEMORY ############")
                print("ALURESULTM ", ALURESULTM)
                print("WA3M ", WA3M)
                print("WRITEDATAM ", WRITEDATAM)
                print("IMMEDIATENEEDM ", IMMEDIATE_NEEDM)
                print("VECTORSNEEDM ", VECTORS_NEEDM)
                print("OPM ", OPM)
                print("CMDM ", CMDM)
                print("LM ", LM)
                time.sleep(1)

    def noClock(self):
        global clock, ALURESULT_M, WRITEDATA_M, WA3_M, IMMEDIATE_NEED_M, VECTORS_NEED_M, OP_M, CMD_M, L_M, RD1_M, RD2_M, RDV1_M, RDV2_M, RD_M, IMMEDIATE_M, READ_M
        global ALURESULTM, WRITEDATAM, WA3M, IMMEDIATE_NEEDM, VECTORS_NEEDM, OPM, CMDM, LM, RD1M, RD2M, RDV1M, RDV2M, RDM, IMMEDIATEM, READM
        global INSTRUCTION_MEMORY, MEMORY_ARRAY
        if(clock == 1):
            if(CMD_M != ''):
                self.aluresultm = ALURESULT_M
                self.readm = READ_M
                self.wa3m = WA3_M
                self.writedatam = WRITEDATA_M
                self.immediateNeedm = IMMEDIATE_NEED_M
                self.vectorsNeedm = VECTORS_NEED_M
                self.opm = OP_M
                self.cmdm = CMD_M
                self.lm = L_M
            print()
            print("############ MEMORY ############")
            print("ALURESULT_M ", self.aluresultm)
            print("WA3_M ", self.wa3m)
            print("WRITEDATA_M ", self.writedatam)
            print("IMMEDIATENEED_M ", self.immediateNeedm)
            print("VECTORSNEED_M ", self.vectorsNeedm)
            print("OP_M ", self.opm)
            print("CMD_M ", self.cmdm)
            print("L_M ", self.lm)

        else:
            if(self.opm == '00'):
                if(self.immediateNeedm == '0'):
                    if(self.vectorsNeedm == '0'):
                        ALURESULTM = self.aluresultm
                        WA3M = self.wa3m
                        WRITEDATAM = ''
                        IMMEDIATE_NEEDM = self.immediateNeedm
                        VECTORS_NEEDM = self.vectorsNeedm
                        LM = self.lm
                        OPM = self.opm
                        CMDM = self.cmdm
                    elif(self.vectorsNeedm == '1'):
                        ALURESULTM = self.aluresultm
                        WA3M = self.wa3m
                        WRITEDATAM = ''
                        IMMEDIATE_NEEDM = self.immediateNeedm
                        VECTORS_NEEDM = self.vectorsNeedm
                        LM = self.lm
                        OPM = self.opm
                        CMDM = self.cmdm
                elif(self.immediateNeedm == '1'):
                    if(self.vectorsNeedm == '0'):
                        ALURESULTM = self.aluresultm
                        WA3M = self.wa3m
                        WRITEDATAM = ''
                        IMMEDIATE_NEEDM = self.immediateNeedm
                        VECTORS_NEEDM = self.vectorsNeedm
                        LM = self.lm
                        OPM = self.opm
                        CMDM = self.cmdm
                    elif(self.vectorsNeedm == '1'):
                        ALURESULTM = self.aluresultm
                        WA3M = self.wa3m
                        WRITEDATAM = ''
                        IMMEDIATE_NEEDM = self.immediateNeedm
                        VECTORS_NEEDM = self.vectorsNeedm
                        LM = self.lm
                        OPM = self.opm
                        CMDM = self.cmdm
            elif(self.opm == '01'):
                if(self.vectorsNeedm == '0'):
                    if(self.lm == '0'): # STR
                        data = toDecimal(self.writedatam[0][0] + self.writedatam[1][0] + self.writedatam[2][0] + self.writedatam[3][0])
                        print("DATA", data)
                        print("INSTRUCTION MEMORY ", MEMORY_ARRAY[data])
                        print("ALURESULTM ", self.aluresultm)
                        MEMORY_ARRAY[data] = self.aluresultm
                        ALURESULTM = ''
                        WA3M = ''
                        WRITEDATAM = ''
                        IMMEDIATE_NEEDM = self.immediateNeedm
                        VECTORS_NEEDM = self.vectorsNeedm
                        LM = self.lm
                        OPM = self.opm
                        CMDM = self.cmdm
                    elif(self.lm == '1'): # LDR
                        print("WRITEDATA IN MEMORY ", self.writedatam)
                        print("LDRV WRITEDATA", self.wa3m)
                        print("LDRV ALURESULT ", self.aluresultm)
                        data = toDecimal(self.aluresultm[0][0] + self.aluresultm[1][0] + self.aluresultm[2][0] + self.aluresultm[3][0])
                        ALURESULTM = MEMORY_ARRAY[data]
                        WRITEDATAM = ''
                        WA3M = self.wa3m
                        IMMEDIATE_NEEDM = self.immediateNeedm
                        VECTORS_NEEDM = self.vectorsNeedm
                        LM = self.lm
                        OPM = self.opm
                        CMDM = self.cmdm
                elif(self.vectorsNeedm == '1'):
                    if(self.lm == '0'): # STRV
                        data = toDecimal(self.writedatam[0][0] + self.writedatam[1][0] + self.writedatam[2][0] + self.writedatam[3][0])
                        MEMORY_ARRAY[data] = [self.aluresultm[0] , self.aluresultm[1], self.aluresultm[2], self.aluresultm[3]]
                        MEMORY_ARRAY[data + 1] = [self.aluresultm[4] , self.aluresultm[5], self.aluresultm[6], self.aluresultm[7]]
                        ALURESULTM = ''
                        WA3M = ''
                        WRITEDATAM = ''
                        IMMEDIATE_NEEDM = self.immediateNeedm
                        VECTORS_NEEDM = self.vectorsNeedm
                        LM = self.lm
                        OPM = self.opm
                        CMDM = self.cmdm 
                    elif(self.lm == '1'): # LDRV
                        print("WRITEDATA IN MEMORY ", self.writedatam)
                        print("LDRV WRITEDATA", self.wa3m)
                        print("LDRV ALURESULT ", self.aluresultm)
                        data = toDecimal(self.aluresultm[0][0] + self.aluresultm[1][0] + self.aluresultm[2][0] + self.aluresultm[3][0])
                        aluTemp = MEMORY_ARRAY[data] + MEMORY_ARRAY[data + 1]
                        print("MEMORY ARRAY 0", MEMORY_ARRAY[data])
                        print("MEMORY ARRAY 0", MEMORY_ARRAY[data + 1])
                        print("MEMORY ARRAY 0", MEMORY_ARRAY[data + 2])
                        print("MEMORY ARRAY 0", MEMORY_ARRAY[data + 3])
                        ALURESULTM = aluTemp
                        WRITEDATAM = ''
                        WA3M = self.wa3m
                        IMMEDIATE_NEEDM = self.immediateNeedm
                        VECTORS_NEEDM = self.vectorsNeedm
                        LM = self.lm
                        OPM = self.opm
                        CMDM = self.cmdm
            print()
            print("############ NO MEMORY ############")
            print("ALURESULTM ", ALURESULTM)
            print("WA3M ", WA3M)
            print("WRITEDATAM ", WRITEDATAM)
            print("IMMEDIATENEEDM ", IMMEDIATE_NEEDM)
            print("VECTORSNEEDM ", VECTORS_NEEDM)
            print("OPM ", OPM)
            print("CMDM ", CMDM)
            print("LM ", LM)
            # print("NOT MEMORY CLOCK")

    def loadImage(self):
        # Can be many different formats.
        im = Image.open('../images/lenna_grises128.jpg', 'r')
        pix_val = list(im.getdata())
        # print(pix_val[16383])
        size = im.size
        size_2 = len(pix_val)
        print(size_2)
        print("SIZE IMAGE ", size)
        cont = 0
        
        # for x in pix_val:
        #     print(x)
        while(cont < size_2 * 10):
            mem_l = []
            if(cont < size_2):
                if(cont == size_2 - 4):
                    # print("PIXEL 1 ", pix_val[cont])
                    # print("PIXEL 2 ", pix_val[cont+1])
                    # print("PIXEL 3 ", pix_val[cont+2])

                    l1 = pix_val[cont]
                    l2 = pix_val[cont+1]
                    l3 = pix_val[cont+2]

                    mem_l.append([toBinary(l1, 8)])
                    mem_l.append([toBinary(l2, 8)])
                    mem_l.append([toBinary(l3, 8)])
                    mem_l.append([toBinary(0, 8)])

                    MEMORY_ARRAY.append(mem_l)
                else:

                    # print("PIXEL 1 ", pix_val[cont])
                    # print("PIXEL 2 ", pix_val[cont+1])
                    # print("PIXEL 3 ", pix_val[cont+2])
                    # print("PIXEL 4 ", pix_val[cont+3])

                    l1 = pix_val[cont]
                    l2 = pix_val[cont+1]
                    l3 = pix_val[cont+2]
                    l4 = pix_val[cont+3]

                    mem_l.append([toBinary(l1, 8)])
                    mem_l.append([toBinary(l2, 8)])
                    mem_l.append([toBinary(l3, 8)])
                    mem_l.append([toBinary(l4, 8)])

                    MEMORY_ARRAY.append(mem_l)

            else:
                mem_l.append([toBinary(0, 8)])
                mem_l.append([toBinary(0, 8)])
                mem_l.append([toBinary(0, 8)])
                mem_l.append([toBinary(0, 8)])

                MEMORY_ARRAY.append(mem_l)

            cont += 4

        # print(MEMORY_ARRAY)
        # print(len(MEMORY_ARRAY))

    

################################## WRITE BACK ##################################


class WriteBack:
    def __init__(self):
        self.aluresult_w = ''
        self.wa3_w = ''
        self.immediateNeed_w = ''
        self.vectorsNeedw_w = ''
        self.op_w = ''
        self.cmd_w = ''
        self.l_w = ''

    def start(self):
        global clock, ALURESULT_W, WA3_W, IMMEDIATE_NEED_W, VECTORS_NEED_W, OP_W, CMD_W, L_W
        global vectorsFile, registerFile, MEMORY_ARRAY
        while(True):
            if(clock):
                if(CMD_W != ''):
                    self.aluresult_w = ALURESULT_W
                    self.wa3_w = WA3_W
                    self.immediateNeed_w = IMMEDIATE_NEED_W
                    self.vectorsNeedw_w = VECTORS_NEED_W
                    self.op_w = OP_W
                    self.cmd_w = CMD_W
                    self.l_w = L_W

                print()
                print("############ WRITEBACK ############")
                print("ALURESULT_W", self.aluresult_w)
                print("WA3_W", self.wa3_w)
                print("IMMEDIATE_NEED_W", self.immediateNeed_w)
                print("VECTORS_NEED_W", self.vectorsNeedw_w)
                print("OP_W", self.op_w)
                print("CMD_W", self.cmd_w)
                print("L_W", self.l_w)
                time.sleep(1)
            else:
                if(CMD_W != ''):
                    if(self.op_w == '00'):
                        if(self.vectorsNeedw_w == '0'):
                            registerFile.noClock('','',self.wa3_w, 1, self.aluresult_w)
                        elif(self.vectorsNeedw_w == '1'):
                            vectorsFile.noClock('', '', self.wa3_w, 1, self.aluresult_w)
                    elif(self.op_w == '01'):
                        if(self.l_w == '1'):
                            if(self.vectorsNeedw_w == '0'):
                                registerFile.noClock('', '', self.wa3_w, 1, self.aluresult_w)
                                print("LDR")
                            elif(self.vectorsNeedw_w == '1'):
                                print("LDRV")
                                vectorsFile.noClock('', '', self.wa3_w, 1, self.aluresult_w)
                print()
                print("############ NO WRITEBACK ############")
                print(MEMORY_ARRAY[4094])
                print(MEMORY_ARRAY[4096])
                time.sleep(1)

    def noClock(self):
        global clock, ALURESULT_W, WA3_W, IMMEDIATE_NEED_W, VECTORS_NEED_W, OP_W, CMD_W, L_W
        global vectorsFile, registerFile, MEMORY_ARRAY

        if(clock == 1):

            if(CMD_W != ''):
                self.aluresult_w = ALURESULT_W
                self.wa3_w = WA3_W
                self.immediateNeed_w = IMMEDIATE_NEED_W
                self.vectorsNeedw_w = VECTORS_NEED_W
                self.op_w = OP_W
                self.cmd_w = CMD_W
                self.l_w = L_W

            print()
            print("############ WRITEBACK ############")
            print("ALURESULT_W", self.aluresult_w)
            print("WA3_W", self.wa3_w)
            print("IMMEDIATE_NEED_W", self.immediateNeed_w)
            print("VECTORS_NEED_W", self.vectorsNeedw_w)
            print("OP_W", self.op_w)
            print("CMD_W", self.cmd_w)
            print("L_W", self.l_w)

            # print("WRITEBACK CLOCK")
        else:
            if(CMD_W != ''):
                if(self.op_w == '00'):
                    if(self.vectorsNeedw_w == '0'):
                        registerFile.noClock('','',self.wa3_w, 1, self.aluresult_w)
                    elif(self.vectorsNeedw_w == '1'):
                        vectorsFile.noClock('', '', self.wa3_w, 1, self.aluresult_w)
                elif(self.op_w == '01'):
                    if(self.l_w == '1'):
                        if(self.vectorsNeedw_w == '0'):
                            registerFile.noClock('', '', self.wa3_w, 1, self.aluresult_w)
                            print("LDR")
                        elif(self.vectorsNeedw_w == '1'):
                            print("LDRV")
                            vectorsFile.noClock('', '', self.wa3_w, 1, self.aluresult_w)
            print()
            
            print("############ NO WRITEBACK ############")
            print(MEMORY_ARRAY[0])
            print(MEMORY_ARRAY[1])
            print(MEMORY_ARRAY[2])
            print(MEMORY_ARRAY[3])
            print(MEMORY_ARRAY[4])
            print(MEMORY_ARRAY[5])
            # print(MEMORY_ARRAY[4094])
            # print(MEMORY_ARRAY[4098])
            # print("NOT WRITEBACK CLOCK")


################################## MAIN ##################################

def main():
    global FLAG_PROCESSOR
    global clock
    global REGISTERS, VECTORS, MEMORY_ARRAY
    print("Do you want to run it you or all???\n")
    x = input("1. All or 2. You: ")

    


    # while(FLAG_PROCESSOR):
    #     x = input("")
    #     print("clock: " + str(clock))
    #     if(str(x) == "0"):

    #         if(clock == 0):
    #             fetch.noClock()
    #             pFD.noClock()
    #             decode.noClock()
    #             pDE.noClock()
    #             execute.noClock()
    #             pEM.noClock()
    #             memory.noClock()
    #             pMW.noClock()
    #             wb.noClock()
    #             clock = 1
    #         elif(clock == 1):
    #             fetch.noClock()
    #             pFD.noClock()
    #             decode.noClock()
    #             pDE.noClock()
    #             execute.noClock()
    #             pEM.noClock()
    #             memory.noClock()
    #             pMW.noClock()
    #             wb.noClock()
    #             print("REGISTERS ", REGISTERS)
    #             print()
    #             print("VECTORS ", VECTORS)
    #             print()
    #             print("MEMORY POSITION 0 ", MEMORY_ARRAY[0])
    #             clock = 0
    #     else:
    #         FLAG_PROCESSOR = False
    #     print()

    mem = Memory()
    mem.loadImage()

    if(str(x) == "1"):

        clk = Clock()
        fetch = Fetch()
        decode = Decode()
        execute = Execute()
        memory = Memory()
        wb = WriteBack()
        pDE = pipeDE()
        pFD = pipeFD()
        pEM = pipeEM()
        pMW = pipeMW()
        fetch.startInstructionMemory()
        memory.loadImage()
        print()
        print(len(MEMORY_ARRAY))
        print(MEMORY_ARRAY[0])
        print("One by one")

        t_clock = threading.Thread(target=clk.start)
        t_fetch = threading.Thread(target=fetch.start)
        t_pDE = threading.Thread(target=pDE.start)
        t_decode = threading.Thread(target=decode.start)
        t_pFD = threading.Thread(target=pFD.start)
        t_execute = threading.Thread(target=execute.start)
        t_pEM = threading.Thread(target=pEM.start)
        t_mem = threading.Thread(target=memory.start)
        t_pMW = threading.Thread(target=pMW.start)
        t_wb = threading.Thread(target=wb.start)

        t_clock.start()
        time.sleep(0.1)

        t_fetch.start()
        time.sleep(0.1)

        t_pFD.start()
        time.sleep(0.1)

        t_decode.start()
        time.sleep(0.1)

        t_pDE.start()
        time.sleep(0.1)

        t_execute.start()
        time.sleep(0.1)

        t_pEM.start()
        time.sleep(0.1)

        t_mem.start()
        time.sleep(0.1)

        t_pMW.start()
        time.sleep(0.1)

        t_wb.start()

    elif(str(x) == "2"):

        fetch = Fetch()
        decode = Decode()
        execute = Execute()
        memory = Memory()
        wb = WriteBack()
        pDE = pipeDE()
        pFD = pipeFD()
        pEM = pipeEM()
        pMW = pipeMW()
        fetch.startInstructionMemory()
        memory.loadImage()
        print()
        print(len(MEMORY_ARRAY))
        print(MEMORY_ARRAY[0])
        print("One by one")

        while(FLAG_PROCESSOR):
            x = input("")
            if(str(x) == "0"):

                if(clock == 0):
                    fetch.noClock()
                    pFD.noClock()
                    decode.noClock()
                    pDE.noClock()
                    execute.noClock()
                    pEM.noClock()
                    memory.noClock()
                    pMW.noClock()
                    wb.noClock()
                    clock = 1
                elif(clock == 1):
                    fetch.noClock()
                    pFD.noClock()
                    decode.noClock()
                    pDE.noClock()
                    execute.noClock()
                    pEM.noClock()
                    memory.noClock()
                    pMW.noClock()
                    wb.noClock()
                    print(REGISTERS)
                    print()
                    print(VECTORS)
                    print()
                    clock = 0
            else:
                FLAG_PROCESSOR = False
            print("clock: " + str(clock))

    else:
        print("Error")


main()
# toBinary(1, 4)
