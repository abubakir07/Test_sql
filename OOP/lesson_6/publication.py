# class Publication:

#     def __init__(self, name, date, pages, library, types):
#         self.name = name
#         self.date = date
#         self.pages = pages
#         self.library = library
#         self.types = types

#         def get_code_in_library(self):
#             return [
#                 f'{self.library[:2]}'
#                 f'{self.name[:2]}'
#                 f'{self.types}'
#                 f'{self.pages}'
#                 f'{''.join{self.date}}'
#             ]


# class Book(Publication):
    
#     def bok(self):
#         self.type = 'book'
#         return self.type

# class Magazine(Publication):

#     def bok(self):
#         self.type = 'magazine'
#         return self.type
    
# class Newspaper(Publication):

#     def bok(self):
#         self.type = 'newspaper'
#         return self.type

######################################
# class AirPlane:
#     def __init__(self, make, model, year, max_speed):
#         self.make = make
#         self.model = model
#         self.make = year
#         self.max_speed = max_speed 
#         self.odometer = 0
#         self.is_flying = False

#     def take_off(self):
#         self.is_flying = True 
    
#     def land(self):
#         self.is_flying = False

#     def fly(self, km):
#         self.odometer += km

# je = AirPlane('F', '15', 2000, 1000)


class Weapon:
    def __init__(self, name, model, max_shop, range, color, weight):
        self.name = name
        self.model = model
        self.max_shop = max_shop
        self.range = range
        self.color = color
        self.weight =weight
        # self.bullets = 0

    def fill_ammo(self, bullets):
        self.max_shop += bullets
    def fire(self, bullets):
        self.max_shop-= bullets
    def change_color(self, new_color):
        self.new_color = input()
        self.color = new_color
    def add_extension(self):
        self.