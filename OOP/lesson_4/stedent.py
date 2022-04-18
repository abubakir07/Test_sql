# class Our_Student:
    
#     def __init__(self, name, sfera):
#         self.name = name
#         self.sfera = sfera
#         self.books = []
#         self.knowledge = 0
#         self.is_ready_to_work = False
#         self.language = {}
#     
#     def ready_book(self, book):
#         self.books.append(book)
#         self.knowledge+=100

#     def do_homework(self):
#         self.knowledge+=10

#     def do_project(self):
#         self.knowledge+=50

#     def add_points(self, value):
#         self.knowledge+value
#         if self.knowledge > 1000:
#             self.is_ready_to_work = True
#             print('Этот студент готов к работе')
            
#     def learn_new_language(self, languge, percent):
#         if percent > 1 and percent <= 100:
#             self.language[languge] = percent
#         else:
#             raise ValueError

#     def info(self):
#         return f'Name: {self.name}\nSfera: {self.sfera}\n'
        
# Abu = Our_Student('Abubakir', 'Beckend')
# Abu.ready_book('Mumu')
# Abu.learn_new_language('Python', 20)

####################################################################################

# class Person:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age 
#         self.money = 0
#         self.house = False

#     def info(self):
#         return f'Name: {self.name}\nage: {self.age}\nmoney: {self.money}\nhouse: {self.house}'
    
#     def earn_money(self, coin):
#         self.money+=coin
#     def buy_house(self, n_house, discount):
#         price = n_house.f_price(discount)
#         if self.money >= price:
#             self.money -= price
#             self.n_house = n_house


# class House:
#     def __init__(self, S, price):
#         self.S = S
#         self.price  = price
    
#     def f_price(self, discount):
#         f_price = self.price - (self.price * discount / 100)
#         print(f'Final price: {f_price}')
#         return f_price
    
#     # def discount(self, dcount):
#     #     self.stoim -= dcount

# class Tip_House(House):
#     def __init__(self, price):
#         self.S = '40m2'
#         self.price  = price

# abu = Person('Abubakir', 15)
# abu.earn_money(5000)
# print(abu.info())

#################################################################################

from multiprocessing import BufferTooShort


class Tomato:
    lvl = {0: 'nothing', 1: 'flower', 2: 'green_tomato', 3: 'red_tomato'}
    def __init__(self, index):
        self.index = index
        self.lvl = 0
    
    def info(self):
        f"""
        Index: {self.index},
        Level: {self.lvl}
        """
    def grow(self):
        self.state_lvl()

    def is_ripe(self):
        if self.lvl == 3:
            return True
        return False
 
    def state_lvl(self):
        if self.lvl < 3:
            self.lvl += 1
            self.level()

class Bush:

    def __init__(self, num):
            self.tomats = [Tomato(index) for index in range(0, num)]

    def grow_all(self):
        for tomato in self.tomats:
            tomato.grow()

            
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomats])

            
    def all_p(self):
        self.tomats = []




class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self.plant = plant

    def work(self):
        self.plant.grow_all()

    def harvest(self):
            if self.plant.all_are_ripe():
                self.plant.all_are_ripe() + self.all_p()
                print('раюота окончена')
            else:
                print('хихихиха')

if __name__ == '__main__':
    # great_tomato_bush = Bush(4)
    gardener = Gardener('Emma',  Bush(4))
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()
        


