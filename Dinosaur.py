from Robot import robot
from Weapon import weapon


class dinosaur:

    def __init__(self):
        
        self.name = 'Rex'
        self.attack_power = 0
        self.health = 100

    def attacks(self, name, attack_power):
        self.name = name()
        attack_power = attack_power


    def attack(self, robot):
        if robot.weapons == "" or robot.weapons == "":
           robot.health_points -= self.attack_power *.15