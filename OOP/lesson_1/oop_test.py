# class Person:

#     def __init__(self,name,age,gender,weight):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.weight = weight

#     def info(self):

# class Teacher:

#     def __init__(self, name, age, lessons, salary):
#         self.name = name
#         self.age = age
#         self.lessons = lessons
#         self.salary = salary

#     def info(self):
#         return f'name: {self.name}\nage: {self.age}\nlessons: {self.lessons}\nsalary: {self.salary}'
# baba = Teacher('Altynay', '38','Russian' ,'15000')
# print(baba.info())
class Car:

    def __init__(self, mark, model, color, year):
        self.mark = mark
        self.model = model
        self.color = color
        self.year = year
        self.fuel = 500
        self.odometr = 0
        self.is_going = False
    
    def start(self, km):
        if self.fuel <= 0:
            self.is_going = False
            print('No fuel!')
        else:
            if self.fuel - km * 12 >= 0:
                print('no fuel')
            else:
                self.is_going = True
                self.odometr += km
                self.fuel -= km * 12
            
                
                
            
            print(f'{self.mark} is going {self.odometr}')

    def stop(self):
        self.is_going = False

t34 = Car('tank', 't34', 'pink', 1940)
for i in range(10):
    t34.start(6)
    print(t34.fuel)