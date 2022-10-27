from Weapon import Weapon


class Jaeger:
    def __init__(self, name):
        self.hp = 100
        self.name = name
        self.weapon_list = []
        self.active_weapon = None
        pass

# class Jaeger:
       # def __init__(self, name):
        # self.name = name
        # self.health = 150
        # self.weapon = Weapon('auto-cannon', 15)

        # def attack_kaiju(self, kaiju):
        # kaiju.health -= self.weapon.attack_power

        # print(f'{self.name}! That {kaiju.name} took a huge hit with that {self.weapon.name}, for {self.weapon.attack_power}. Our thermal scans are showing that its energy levels are down to {kaiju.health}')
