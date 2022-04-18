# class Player:
#     playlist = []
#     def show(self):
#         return self.playlist
#     def add(self, value):
#         self.playlist.append(value)
#     def play(self):
#         for i in self.playlist:
#             print()
#     def delete(self, value):
#         self.playlist.remove(value)


# class AudioPlayer(Player):
#     pass

# class VideoPlayer(Player):
#     pass


##############################


class Animal:

    def eat(self):
        return 'gam-gam!'
    def sleep(self):
        return 'zzz-zzz'
    def make_sound(self):
        pass

class AnimalWithHorn(Animal):
    def gore(self):
        return 'afsefafafwaf'

class Cow(AnimalWithHorn):
    def make_sound(self):
        return "mu-mu"

class Ram(AnimalWithHorn):
    def make_sound(self):
        return 'be-be'
cow = Cow()
print(cow.eat())
print(cow.sleep())
print(cow.make_sound())
print(cow.gore())
print('########################')
ram = Ram()
print(ram.eat())
print(ram.sleep())
print(ram.make_sound())
print(ram.gore())
