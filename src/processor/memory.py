from PIL import Image


class Memory:
    def __init__(self, A, RD, WE, FLAG_PROCESSOR):

        self.A = A
        self.RD = RD
        self.WE = WE
        self.FLAG_PROCESSOR = FLAG_PROCESSOR

    def start(self, clock):

        while(self.FLAG_PROCESSOR):
            if(clock):
                print("USING CLOCK")
            else:
                print("NOT USING CLOCK")
