class Hero:
    jumlahHero = 0  # public , static property

    __privateJumlah = 100  # private static

    def __init__(self, inputName, inputHealth, inputPower, inputDefense, speed):
        self.__name = inputName  # private , object property
        self.__health = inputHealth  # private , object property
        self.__power = inputPower  # private , object property
        self.__defense = inputDefense  # private , object property

        self.__speed = speed

        Hero.jumlahHero += 1

    @staticmethod  # method yang bisa di akses oleh object dan class
    def getPrivateJumlah():  # static method
        return Hero.__privateJumlah

    @classmethod  # decorator. hanya bisa diakses oleh class
    def getPrivateJumlah1(cls):  # harus cls kalau class method
        return cls.__privateJumlah

    def introduce(self):
        print("my name is "+self.__name)

    # setter

    def setName(self, name):
        self.__name = name

    # getter
    def getName(self):
        return self.__name

    def setPower(self, power):
        self.__power = power

    def getPower(self):
        return self.__power

    def setHealth(self, point):
        self.__health += point

    def getHealth(self):
        return self.__health

    def setDefense(self, defense):
        self.__defense = defense

    def getDefense(self):
        return self.__defense

    @property
    def speed(self):
        pass

    @speed.getter
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, input):
        self.__speed = input

    @speed.deleter
    def speed(self):
        print("Speed di delete")
        self.__speed = None

    def attacking(self, heroInstance):

        if(self.getPower() <= 0):
            print(self.getName()+" LOSE ")
            return 0

        result = self.getPower() - heroInstance.getDefense()

        if result >= 0:
            result = result * -1
            heroInstance.setHealth(result)

            print(self.getName(), "attacking ",
                  heroInstance.getName(), "with ", self.getPower())
            print(heroInstance.getName(), " loses ", result, " health")
            print("=====================================")
        else:
            print(self.getName(), "attacking ",
                  heroInstance.getName(), "with ", self.getPower(), "power ", "NO EFFECT !! ")

            print("=====================================")
