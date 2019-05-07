from PIL import Image
import threading
import time

clock = 0
FLAG_PROCESSOR = True
A = 0
RD = 0
WE = 0


MEMORY_ARRAY = []


def toBinary(number, zeros):
    binary = bin(number)
    resBinary = binary[2:]
    print(resBinary)
    if(len(resBinary) < zeros):
        n = zeros - len(resBinary)
        cont = 0
        res = ''
        while(cont < n):
            res += '0'
            cont += 1

        res += resBinary
        print(res)
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

        print(res)
        return res
    else:
        print(resBinary)
        return resBinary


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


class Fetch:

    def start(self):
        global clock
        while(True):
            if(clock):
                print("FETCH CLOCK")
                time.sleep(1)
            else:
                print("NOT FETCH CLOCK")
                time.sleep(1)

    def startInstructionMemory(self):
        print()

    def noClock(self):
        global clock
        if(clock == 1):
            print("FETCH CLOCK")
        else:
            print("NOT FETCH CLOCK")


class Decode:

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
        global clock
        if(clock == 1):
            print("DECODE CLOCK")
        else:
            print("NOT DECODE CLOCK")


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


def main():
    global FLAG_PROCESSOR
    global clock
    print("Do you want to run it you or all???\n")
    x = input("1. All or 2. You: ")

    mem = Memory()
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


# main()
toBinary(200, 12)
