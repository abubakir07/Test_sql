# class Human:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
    
#     def info(self):
#         print(self.name, self.__age)

#     # def set_age(self,x):
#     #     self.__age=x
#     #     return self.__age

#     @property
#     def age(self):
#         return self.__age

#     @age.setter
#     def age(self,x):
#         if 0<x<=200:
#             self.__age=x

# h=Human('Aziret',18)
# print(h.__dir__())
# h.age=120
# h.info()
##############################
#ISINSTANCE
# class Rectangle:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

#     def get_rect_area(self):
#         return self.a*self.b

# class Square:
#     def __init__(self,a):
#         self.a=a

#     def get_square_area(self):
#         return self.a**2

# class Circle:
#     def __init__(self,a):
#         self.a=a

#     def get_circle_area(self):
#         return 3.14*self.a**2

    
# rect1=Rectangle(12,15)
# rect2=Rectangle(7,5)
# sq1=Square(5)
# sq2=Square(7)
# circ1=Circle(12)
# circ2=Circle(6)

# figures=[rect1,rect2,sq1,sq2,circ1,circ2]
# for fig in figures:
#     if isinstance(fig,Rectangle):
#         print(fig.get_rect_area())
#     elif isinstance(fig,Square):
#         print(fig.get_square_area())
#     elif isinstance(fig,Circle):
#         print(fig.get_circle_area())
#########################################
#Polimorfizm
class Rectangle:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def get_area(self):
        return self.a*self.b

class Square:
    def __init__(self,a):
        self.a=a
    def get_area(self):
        return self.a**2

class Circle:
    def __init__(self,a):
        self.a=a
    def get_area(self):
        return 3.14*self.a**2

rect1=Rectangle(12,15)
rect2=Rectangle(7,5)
sq1=Square(5)
sq2=Square(7)
circ1=Circle(12)
circ2=Circle(6)

figures=[rect1,rect2,sq1,sq2,circ1,circ2]
for fig in figures:
    print(fig.get_area())
    
