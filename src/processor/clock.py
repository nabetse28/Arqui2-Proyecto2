import time


class Clock:
    def start(self, clock):
        print("Do you want to run it you or all???\n")
        x = input("1. You or 2. All: ")
        print(str(x))
        if(str(x) == "1"):
            print("All")
            flag = True

            while(flag):
                x = input("")
                if(str(x) == "0"):
                    flag = True
                    if(clock == 0):
                        clock = 1
                    elif(clock == 1):
                        clock = 0
                else:
                    flag = False

                print("clock: " + str(clock))

        elif(str(x) == "2"):
            print("All")
            flag = True
            clock = 0
            while(flag):
                if(clock == 0):
                    clock = 1
                elif(clock == 1):
                    clock = 0
                time.sleep(1)
                print("clock: " + str(clock))
        else:
            print("Error")
