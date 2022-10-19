from Weapon import weapon

class robot:

    def __init__(self):
        self.name = 'Chicken'
        self.health = 100
        self.active_weapon = weapon('Sword', 22)
        self.weapons_list = ['sword']

    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power 