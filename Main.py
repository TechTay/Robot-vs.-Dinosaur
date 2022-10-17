from Battlefield import battlefield
from Robot import robot
from Dinosaur import dinosaur
from Weapon import weapon

# Start the game!
print('\n')
battlefield_one = battlefield()
battlefield_one.Run_game()
battlefield_one.display_welcome()



weapon_one = weapon()
weapon_two = weapon()
weapon_three = weapon()

weapon_one.weapons('Staff', 10)
weapon_two.weapons('Sword', 12)
weapon_three.weapons('Hammer', 15)

battlefield_one.battle_phase()

