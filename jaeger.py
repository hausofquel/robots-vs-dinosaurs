from weapon import Weapon

from random import Random

class Jaeger:
    def __init__(self, name):
        self.name = name
        self.health = 150
        self.weapon = Weapon('auto-cannon', 15)

    def __init__(self, name):
        self.name = name
        self.health = 150
        self.weapon = Weapon('lightning-blade', 30)

    def attack_kaiju(self, kaiju):
        kaiju.health -= self.weapon.attack_power

        print(f'{self.name}! That {kaiju.name} took a huge hit with that {self.weapon.name}, for {self.weapon.attack_power}. Our thermal scans are showing that its energy levels are down to {kaiju.health}')


