
from Weapon import weapon


class dinosaur:

    def __init__(self):
        
        self.name = 'Rex'
        self.attack_power = 25
        self.health = 100

    def attack(self, robot):
        robot.health -= self.attack_power 