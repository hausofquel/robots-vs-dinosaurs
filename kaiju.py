from random import Random


class Kaiju:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = 40
        self.health = 200

    def attack_jaeger(self, jaeger):
        jaeger.health -= self.attack_power

        print(f'{jaeger.name} you took {self.attack_power}, from a {kaiju.name}! Your energy levels are down to {jaeger.health}! Fall back! Fall back!')
