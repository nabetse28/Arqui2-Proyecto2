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
RDV1 = ''

IMMEDIATE_NEED = ''
VECTORS_NEED = ''
IMMEDIATE = ''
RD = ''



MEMORY_ARRAY = []
INSTRUCTION_MEMORY = []
REGISTERS = {"0000": [], "0001": [], "0010": [], "0011": [],
             "0100": [], "0101": [], "0110": [], "0111": [],
             "1000": [], "1001": [], "1010": [], "1011": [],
             "1100": [], "1101": [], "1110": [], "1111": []}

VECTORS = {"0000": [], "0001": [], "0010": [], "0011": [],
           "0100": [], "0101": [], "0110": [], "0111": [],
           "1000": [], "1001": [], "1010": [], "1011": [],
           "1100": [], "1101": [], "1110": [], "1111": []}

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

    def process8Bits(self, srcAE, srcBE, ALUControlE):

        if(ALUControlE == '0100'):
            A = toDecimal(srcAE)
            B = toDecimal(srcBE)
            res = A + B
        elif(ALUControlE == '0010'):
            A = toDecimal(srcAE)
            B = toDecimal(srcBE)
            res = A - B
        elif(ALUControlE == '0001'):
            A = toDecimal(srcAE)
            B = toDecimal(srcBE)
            res = A ^ B
        elif(ALUControlE == '1000'):
            res = circularMoveRight(srcAE, toDecimal(srcBE))
        elif(ALUControlE == '1001'):
            res = circularMoveLeft(srcAE, toDecimal(srcBE))

    def processRegisterImm(self, srcAE, srcBE, ALUControlE):
        if(ALUControlE == '0100'):
            Abin = srcAE[0] + srcAE[1] + srcAE[2] + srcAE[3]
            A = toDecimal(Abin)
            B = toDecimal(srcBE)
            res = A + B
        elif(ALUControlE == '0010'):
            Abin = srcAE[0] + srcAE[1] + srcAE[2] + srcAE[3]
            A = toDecimal(Abin)
            B = toDecimal(srcBE)
            res = A - B
        elif(ALUControlE == '0001'):
            Abin = srcAE[0] + srcAE[1] + srcAE[2] + srcAE[3]
            A = toDecimal(Abin)
            B = toDecimal(srcBE)
            res = A ^ B
        elif(ALUControlE == '1000'):
            Abin = srcAE[0] + srcAE[1] + srcAE[2] + srcAE[3]
            res = circularMoveRight(Abin, toDecimal(srcBE))
        elif(ALUControlE == '1001'):
            Abin = srcAE[0] + srcAE[1] + srcAE[2] + srcAE[3]
            res = circularMoveLeft(Abin, toDecimal(srcBE))


class pipeFD:
    def __init__(self, inst):
        self.inst = inst

    def start(self):
        global clock, INSTD, INSTF
        while(True):
            if(clock):

                if(self.inst != -1):
                    INSTD = self.inst

                print("INSTD IS " + INSTD)
                print(INSTD)

                # print("PIPE FD CLOCK")
                time.sleep(1)
            else:
                print("INSTF IS " + INSTF)
                print(INSTF)
                self.inst = INSTF
                # print("NOT PIPE FD CLOCK")
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
    def __init__(self, immediateNeed, vectorsNeed, rd1, rd2, rdv1, rdv2, imm, rd):
        self.immediateNeed = immediateNeed
        self.vectorsNeed = vectorsNeed
        self.rd1 = rd1
        self.rd2 = rd2 
        self.rdv1 = rdv1
        self.rdv2 = rdv2
        self.imm = imm
        self.rd = rd

    def start(self):
        global clock
        while(True):
            if(clock):

                print("PIPE DE CLOCK")
                time.sleep(1)
            else:
                print("NOT PIPE DE CLOCK")
                time.sleep(1)

    def noClock(self):
        global clock
        if(clock == 1):
            print("PIPE DE CLOCK")
        else:

            print("NOT PIPE DE CLOCK")


class pipeEM:
    def start(self):
        global clock
        while(True):
            if(clock):

                print("PIPE EM CLOCK")
                time.sleep(1)
            else:
                print("NOT PIPE EM CLOCK")
                time.sleep(1)

    def noClock(self):
        global clock
        if(clock == 1):
            print("PIPE EM CLOCK")
        else:
            print("NOT PIPE EM CLOCK")


class pipeMW:
    def __init__(self, pcSrcM, regWriteM, memToRegM):
        self.pcSrcM = pcSrcM
        self.regWriteM = regWriteM
        self.memToRegM = memToRegM

    def start(self):
        global clock
        while(True):
            if(clock):

                print("PIPE MW CLOCK")
                time.sleep(1)
            else:
                print("NOT PIPE MW CLOCK")
                time.sleep(1)

    def noClock(self):
        global clock
        if(clock == 1):
            print("PIPE MW CLOCK")
        else:
            print("NOT PIPE MW CLOCK")


class registerPC:
    def __init__(self, pc):
        self.pc = pc

    def noClock(self):
        global clock, PC, PCF
        if(clock == 1):
            self.pc = PC
            PC = toBinary(toDecimal(self.pc) + 1, 32)
            print("PCF " + PCF)
            # print("REGISTER PC CLOCK")
        else:

            PCF = PC
            print("PCF " + PCF)
            # print("NOT REGISTER PC CLOCK")


################################## FETCH ##################################
class Fetch:
    def __init__(self, A, RD):
        self.A = A
        self.RD = RD
        self.registerPC = registerPC(0)

    def start(self):
        global clock
        while(True):
            if(clock):
                self.registerPC.noClock()
                self.A = PCF
                print("A " + self.A)
                self.RD = INSTRUCTION_MEMORY[toDecimal(self.A)]
                print("INSTRUCTION " + self.RD)
                # print("FETCH CLOCK")
                time.sleep(1)
            else:
                self.registerPC.noClock()
                INSTF = self.RD
                print("WRITE INSTF " + INSTF)
                # print("NOT FETCH CLOCK")
                time.sleep(1)

    def startInstructionMemory(self):
        global INSTRUCTION_MEMORY
        f = open("../compiler/codeBin.rs", "r")

        content = f.read()

        INSTRUCTION_MEMORY = content.split("\n")

        INSTRUCTION_MEMORY = INSTRUCTION_MEMORY[:len(INSTRUCTION_MEMORY)-1]

        print(INSTRUCTION_MEMORY)

    def noClock(self):
        global clock, PCF, INSTF
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
            if(we3 == 1):
                REGISTERS[a3] = [wd3]
                print(REGISTERS[a3])

            elif(a1 != ''):
                self.A1 = a1
                self.A2 = a2
                print(self.A1 , self.A2)


        else:
            RD1 = REGISTERS[self.A1]
            RD2 = REGISTERS[self.A2]
            print(RD1, RD2)

            

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
            if(we3 == 1):
                VECTORS[a3] = [wd3]
                print(VECTORS[a3])

            else:
                self.A1 = a1
                self.A2 = a2
                print(self.A1 , self.A2)


        else:
            RDV1 = VECTORS[self.A1]
            RDV2 = VECTORS[self.A2]
            print(RDV1, RDV2)
        
vectorsFile = VectorsFile('', '', '', '', '')

class Decode:
    def __init__(self, cond, op, i, v, cmd, rn, rd, src):
        self.cond = cond
        self.op = op
        self.i = i
        self.v = v
        self.cmd = cmd
        self.rn = rn
        self.rd = rd
        self.src = src
        self.imm = ''
        self.rd1 = ''
        self.rd2 = ''
        self.rdv1 = ''
        self.rdv2 = ''
        self.rdpipe = ''

    def start(self):
        global clock
        while(True):
            if(clock):

                print("DECODE CLOCK")
                time.sleep(1)
            else:
                print("NOT DECODE CLOCK")
                time.sleep(1)

    def noClock(self):
        global clock, INSTD, RD1, RD2, RDV1, RDV2, RD
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
                    print()
                


                print(self.cond, self.op, self.i, self.v, self.cmd, self.rn, self.rd, self.src)

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
                    elif(self.i == '1'):
                        registerFile.noClock('', '', '', '', '')
                        IMMEDIATE = self.imm 
                        RD = self.rdpipe
                        IMMEDIATE_NEED = self.i
                        VECTORS_NEED = self.v
                        
                elif(self.v == '1'):
                    if(self.i == '0'):
                        vectorsFile.noClock('','', '', '', '')
                        RD = self.rdpipe 
                        IMMEDIATE_NEED = self.i
                        VECTORS_NEED = self.v
                        IMMEDIATE = self.imm 
                    elif(self.i == '1'):
                        vectorsFile.noClock('', '', '', '', '')
                        IMMEDIATE = self.imm 
                        RD = self.rdpipe
                        IMMEDIATE_NEED = self.i
                        VECTORS_NEED = self.v
            elif(self.op == '01'):
                print()
            
            # print("NOT DECODE CLOCK")


################################## EXECUTE ##################################
class Execute:

    def start(self):
        while(True):
            if(clock):
                print("EXECUTE CLOCK")
                time.sleep(1)
            else:
                print("NOT EXECUTE CLOCK")
                time.sleep(1)

    def noClock(self):
        global clock
        if(clock == 1):
            print("EXECUTE CLOCK")
        else:
            print("NOT EXECUTE CLOCK")

################################## MEMORY ##################################


class Memory:

    # def __init__(self, A, RD, WE):

    #     self.A = A
    #     self.RD = RD
    #     self.WE = WE

    def loadImage(self):
        # Can be many different formats.
        im = Image.open('../images/lenna_saturacion.png', 'r')
        pix_val = list(im.getdata())
        print(pix_val[16383])
        size = im.size[0]
        size_2 = size * size
        print(size)
        cont = 0

        while(cont < size_2 * 3):
            mem_l = []
            if(cont < size_2):
                if(cont == size_2 - 4):
                    print(pix_val[cont])
                    print(pix_val[cont+1])
                    print(pix_val[cont+2])

                    l1 = pix_val[cont][0]
                    l2 = pix_val[cont+1][0]
                    l3 = pix_val[cont+2][0]

                    mem_l.append([toBinary(l1, 8)])
                    mem_l.append([toBinary(l2, 8)])
                    mem_l.append([toBinary(l3, 8)])
                    mem_l.append([toBinary(0, 8)])

                    MEMORY_ARRAY.append(mem_l)
                else:

                    print(pix_val[cont])
                    print(pix_val[cont+1])
                    print(pix_val[cont+2])
                    print(pix_val[cont+3])

                    l1 = pix_val[cont][0]
                    l2 = pix_val[cont+1][0]
                    l3 = pix_val[cont+2][0]
                    l4 = pix_val[cont+3][0]

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

    def start(self):
        global clock
        while(True):
            if(clock):
                print("MEMORY CLOCK")
                time.sleep(1)
            else:
                print("NOT MEMORY CLOCK")
                time.sleep(1)

    def noClock(self):
        global clock
        if(clock == 1):
            print("MEMORY CLOCK")
        else:
            print("NOT MEMORY CLOCK")

################################## WRITE BACK ##################################


class WriteBack:

    def start(self):
        global clock
        while(True):
            if(clock):
                print("WRITEBACK CLOCK")
                time.sleep(1)
            else:
                print("NOT WRITEBACK CLOCK")
                time.sleep(1)

    def noClock(self):
        global clock

        if(clock == 1):
            print("WRITEBACK CLOCK")
        else:
            print("NOT WRITEBACK CLOCK")


################################## MAIN ##################################

def main():
    global FLAG_PROCESSOR
    global clock
    print("Do you want to run it you or all???\n")
    x = input("1. All or 2. You: ")

    fetch = Fetch(-1, -1)
    decode = Decode('','','','','','','','')
    pFD = pipeFD(-1)
    fetch.startInstructionMemory()
    print()

    while(FLAG_PROCESSOR):
        x = input("")
        print("clock: " + str(clock))
        if(str(x) == "0"):

            if(clock == 0):
                fetch.noClock()
                pFD.noClock()
                decode.noClock()
                clock = 1
            elif(clock == 1):
                fetch.noClock()
                pFD.noClock()
                decode.noClock()
                clock = 0
        else:
            FLAG_PROCESSOR = False
        print()

    # mem = Memory()
    # mem.loadImage()

    # if(str(x) == "1"):

    #     clk = Clock()
    #     fetch = Fetch()
    #     decode = Decode()
    #     execute = Execute()
    #     memory = Memory(A, RD, WE)
    #     wb = WriteBack()

    #     t_clock = threading.Thread(target=clk.start)
    #     t_fetch = threading.Thread(target=fetch.start)
    #     t_decode = threading.Thread(target=decode.start)
    #     t_execute = threading.Thread(target=execute.start)
    #     t_mem = threading.Thread(target=memory.start)
    #     t_wb = threading.Thread(target=wb.start)

    #     t_clock.start()
    #     time.sleep(0.1)
    #     t_fetch.start()
    #     time.sleep(0.1)
    #     t_decode.start()
    #     time.sleep(0.1)
    #     t_execute.start()
    #     time.sleep(0.1)
    #     t_mem.start()
    #     time.sleep(0.1)
    #     t_wb.start()

    # elif(str(x) == "2"):

    #     fetch = Fetch()
    #     decode = Decode()
    #     execute = Execute()
    #     memory = Memory(A, RD, WE)
    #     wb = WriteBack()
    #     print("One by one")

    #     while(FLAG_PROCESSOR):
    #         x = input("")
    #         if(str(x) == "0"):

    #             if(clock == 0):
    #                 clock = 1
    #             elif(clock == 1):
    #                 fetch.noClock()
    #                 decode.noClock()
    #                 execute.noClock()
    #                 memory.noClock()
    #                 wb.noClock()
    #                 clock = 0
    #         else:
    #             FLAG_PROCESSOR = False
    #         print("clock: " + str(clock))

    # else:
    #     print("Error")


main()
# toBinary(1, 4)
