from numpy import random


class Product():
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        stealable = self.price / self.weight
        if stealable < 0.5:
            return 'Not so stealable...'
        elif stealable >= 0.5 and stealable < 1:
            return 'Kinda stealable'
        else:
            return 'Very stealable!'

    def explode(self):
        exp = self.flammability * self.weight
        if exp < 10:
            return '...fizzle'
        elif exp >= 10 and exp < 50:
            return '...boom!'
        else:
            return '...BABOOM!'


class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability

    def explode(self):
        return '...it\'s a glove.'

    def punch(self):
        if self.weight < 5:
            return 'That tickles.'
        elif self.weight >= 5 and self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
