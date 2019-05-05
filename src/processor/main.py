from PIL import Image
import threading
import time

clock = 0
FLAG_PROCESSOR = True
A = 0
RD = 0
WE = 0


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

    def __init__(self, A, RD, WE):

        self.A = A
        self.RD = RD
        self.WE = WE

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

    if(str(x) == "1"):

        clk = Clock()
        fetch = Fetch()
        decode = Decode()
        execute = Execute()
        memory = Memory(A, RD, WE)
        wb = WriteBack()

        t_clock = threading.Thread(target=clk.start)
        t_fetch = threading.Thread(target=fetch.start)
        t_decode = threading.Thread(target=decode.start)
        t_execute = threading.Thread(target=execute.start)
        t_mem = threading.Thread(target=memory.start)
        t_wb = threading.Thread(target=wb.start)

        t_clock.start()
        time.sleep(0.1)
        t_fetch.start()
        time.sleep(0.1)
        t_decode.start()
        time.sleep(0.1)
        t_execute.start()
        time.sleep(0.1)
        t_mem.start()
        time.sleep(0.1)
        t_wb.start()

        # Can be many different formats.
        # im = Image.open('../images/stormtropper.png', 'r')
        # pix_val = list(im.getdata())
        # print(pix_val)
        # print(pix_val)
        # print(im.size)
    elif(str(x) == "2"):

        fetch = Fetch()
        decode = Decode()
        execute = Execute()
        memory = Memory(A, RD, WE)
        wb = WriteBack()
        print("One by one")

        while(FLAG_PROCESSOR):
            x = input("")
            if(str(x) == "0"):

                if(clock == 0):
                    clock = 1
                elif(clock == 1):
                    fetch.noClock()
                    decode.noClock()
                    execute.noClock()
                    memory.noClock()
                    wb.noClock()
                    clock = 0
            else:
                FLAG_PROCESSOR = False
            print("clock: " + str(clock))

    else:
        print("Error")


main()
