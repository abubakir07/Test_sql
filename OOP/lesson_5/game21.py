import random 

class Cards:
    dct = {
        'heart': 6,
        'heart': 7,
        'heart': 8,
        'heart': 9,
        'heart': 10,
        'heart-Volet': 11,
        'heart-Dama': 12,
        'heart-king': 13,
        'heart-A': 14,

        'romb': 6,
        'romb': 7,
        'romb': 8,
        'romb': 9,
        'romb': 10,
        'romb-Volet': 11,
        'romb-Dama': 12,
        'romb-king': 13,
        'romb-A': 14,

        'clover': 6,
        'clover': 7,
        'clover': 8,
        'clover': 9,
        'clover': 10,
        'clover-Volet': 11,
        'clover-Dama': 12,
        'clover-king': 13,
        'clover-A': 14,

        'leave': 6,
        'leave': 7,
        'leave': 8,
        'leave': 9,
        'leave': 10,
        'leave-Volet': 11,
        'leave-Dama': 12,
        'leave-king': 13,
        'leave-A': 14,
    }

class Player:

    def __init__(self, name):
        self.name = name
        
    def randmr(self):
        