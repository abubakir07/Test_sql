#Насдедование
#Инкапсуляция
    # public
    # protected
    # private
#Полиморфизм

class Cat: # класс с именем
    def __init__(self, name, age): #конструкор класса
        self.name = name # атрибуты класса & динмич. поля
        self.age = age # атрибуты класса & динмич. поля

    def rename(self, value):
        self.name = value

cat1 = Cat('Felix', 2) # экземпляр класса
print(cat1)
print(cat1.name, cat1.age)
cat1.rename('Legion')
print(cat1.name, cat1.age)


