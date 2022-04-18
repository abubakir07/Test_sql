class Animal:
    def __init__(self, name, life=100, damage=0):
        self.name = name
        self.life = life
        self.damage = damage
    
    def set_damage(self):
        return self.damage
    
    def get_damage(self, value):
        self.life -= value
    
class Cat(Animal):
    def mau(self):
        print("myau-myau")
    
    def get_damage(self, value):
        super().get_damage(value)
        print(f"ах ты собака!; Life={self.life}")

class Dog(Animal):
    def gav(self):
        print("gav-gav")
    
    def get_damage(self, value):
        super().get_damage(value)
        print(f"ах ты  шаверма!; Life={self.life}")

cat = Cat('Bob', damage=5)
dog = Dog('Joma', damage=20)

# dog.gav()
# damage = dog.set_damage()
# damage += dog.set_damage()
# cat.get_damage(damage)
# cat.mau()
# damage = cat.set_damage()
# damage += cat.set_damage()
# dog.get_damage(damage)

dog.gav()
cat.get_damage(dog.set_damage())
cat.mau()
dog.get_damage(cat.set_damage())