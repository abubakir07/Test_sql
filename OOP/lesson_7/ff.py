# class MyObject:
#     int_field = 5
#     str_field = “simple string”

# obj1 = MyObject()
# obj2 = MyObject()

# class Person:
#     def __init__(self, name, surename):
#             self.name = name
#             self.surename = surename

#     def info_about_human(self):
#         return self.name, self.surename

# a = Person('Abu', 'Mahamatjanov')
# b = Person('s', 'v')
# c = Person('d', 'k')


class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer=0
        self.fuel=70

    def drive(self,distance):
        if distance/10<=self.fuel:
            self.__add_distance(distance)
            self.__subtract_fuel(distance)
            print("Let's drive!")
        else:
            print("Need more fuel,please,fill more!")
    def __add_distance(self,value):
        self.odometer+=value
    def __subtract_fuel(self,value):
        self.fuel-=value/10

a = Car('ff', 'k', 99)