class Ota:
    def __init__(self, fullname):
        self.fullname = fullname
        self.__money = 0

    def pul_solish(self):
        pass

    def info(self):
        print(f"Egasi: {self.fullname}")
        print(f"Puli: {self.__money}")

o1 = Ota("Aliyev VAli")
o1.info()
