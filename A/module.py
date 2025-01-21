class F:
    def __init__(self):
        pass

    def act(self):
        with open("test.txt", "r") as f:
            mes = f.read()
        #import os
        #mes = os.listdir(".")
        print(mes)
        