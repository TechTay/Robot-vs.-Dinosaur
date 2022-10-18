from Weapon import weapon
from Dinosaur import dinosaur

class robot:

    def __init__(self):
        self.name = 'Chicken'
        self.health = 100
        self.active_weapon = ()

    def weapon(self, name):
        self.name = name

    def attack(self, dinosaur):
        if dinosaur.weapons == "" or dinosaur.weapons == "":
           dinosaur.health_points -= self.attack_power * .12