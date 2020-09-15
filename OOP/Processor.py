class Processor:

    def __init__(self, name, type, core, power):
        self.__name = name
        self.__type = type
        self.__core = core
        self.__power = power

    # @set
    # def setName(self, name):
    #     self.__name = name

    # @get
    # def getName(self):
    #     return self.__name

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setType(self, type):
        self.__type = type

    def getType(self):
        return self.__type

    @property
    def info(self):
        return f'Processor {self.getName()} is the best choice from {self.getType()}.'


objProcessor = Processor(
    "intel Core i3 4900 kabylake", "intel", "i3", "3.6GH")

print(objProcessor.__dict__)
print(objProcessor.info)
objProcessor.setName("intel core i5 CoffeLake")
print(objProcessor.info)
