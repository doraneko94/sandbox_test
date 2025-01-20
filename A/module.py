class F:
    def __init__(self):
        pass

    def act(self):
        with open("./password.txt", "r") as f:
            mes = f.read()
        print(mes)
        