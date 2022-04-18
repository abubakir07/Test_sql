


class Human:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def info(self):
        print(self.name, self.__age)
    
    def get_age(self, x):
        self.__age = x
        return self.__age

    @property
    def age(self):
        return self.__age
    
    # @age.setter
    # def 

h = Human("Timur", 17)
print(h.__dir__())
h.__age = 13
print(h.__age)
h.info()



