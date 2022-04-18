import random
class Cat:
    def  __init__(self, name, hp, cat_damage):
        self.name = name
        self.hp = hp
        self.cat_damage = cat_damage
cat = Cat('Felix', 130, )


class Dog:
    def  __init__(self, name, hp, dog_damage):
        self.name = name
        self.hp = hp
        self.dog_damage = dog_damage
dog = Dog('Simba', 100)

class fight(Cat, Dog):
    while Dog.hp > 0 or Cat.hp > 0:
        cat_damage = random.randint







