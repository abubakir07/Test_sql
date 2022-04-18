import random


class knife:
    def __init__(self, knife_damage):
        self.knife_damage = 3
    def sound(self):
        return 'knife!'

class gun:
    def __init__(self, gun_damage):
        self.gun_damage = 6
    def sound(self):
        return 'gun!'

class spoon:
    def __init__(self, spoon_damage):
        self.spoon_damage = 1
    def sound(self):
        return 'spoon!'

class sword:
    def __init__(self, sword_damage):
        self.sword_damage = 4
    def sound(self):
        return 'sword!' 

class fork:
    def __init__(self, fork_damage):
        self.fork_damage = 2
    def sound(self):
        return 'fork!'

class axe:
    def __init__(self, axe_damage):
        self.axe_damage = 4
    def sound(self):
        return 'axe!'


class Cat:

    def __init__(self,name,hp,uron):
        self.name=name
        self.hp=hp
        self.uron=uron

    # def sound(self):
    #     return 'Myau!'
class Dog:

    def __init__(self,name,hp,uron):
        self.name=name
        self.hp=hp
        self.uron=uron

    def sound(self):
        return 'Gaw!'
dog=Dog('dogdog',100,10)
cat=Cat('Felix',100,10)
    


def fight():
    while dog.hp>0 and cat.hp>0:
        dog_uron=random.randint(1,dog.uron)
        cat_uron=random.randint(1,cat.uron)
        weapon_uron=random.randint

        dog.hp-=cat_uron
        cat.hp-=dog_uron

        # if dog.hp<=0 or cat.hp<=0:
        #     break
        print(f' Dog:Damaged: {dog_uron}, Leaft hp: {dog.hp}\n Cat:Damaged: {cat_uron}, Leaft hp: {cat.hp}\n##########')

        if dog.hp>cat.hp:
            print(f'Dog: {dog.hp}\nCat:{cat.hp}')
            r='Dog Winned!'
        else:
            r='Cat Winned!'
        #     print(f'Dog: {dog.hp}\nCat:{cat.hp}')
    if dog.hp<cat.hp:
        dog.hp=0
    else:
        cat.hp=0
    return f'{r}\nDog: {dog.hp}\nCat:{cat.hp}'
print(fight())