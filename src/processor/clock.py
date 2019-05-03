import time

global cont


class clock:
    def start(self):
        print("Do you want to run it you or all???\n")
        x = input("1. You or 2. All: ")
        print(str(x))
        if(str(x) == "1"):
            print("All")
            flag = True
            cont = 0
            while(flag):
                x = input("")
                if(str(x) == "0"):
                    flag = True
                    if(cont == 0):
                        cont = 1
                    elif(cont == 1):
                        cont = 0
                else:
                    flag = False

                print("cont: " + str(cont))

        elif(str(x) == "2"):
            print("All")
            flag = True
            cont = 0
            while(flag):
                if(cont == 0):
                    cont = 1
                elif(cont == 1):
                    cont = 0
                time.sleep(1)
                print("cont: " + str(cont))
        else:
            print("Error")


x = clock()
x.start()
