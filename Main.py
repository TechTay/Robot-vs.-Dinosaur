from Battlefield import battlefield
from Robot import robot
from Dinosaur import dinosaur
from Weapon import weapon

# Start the game!
print('\n')
battlefield_one = battlefield()
battlefield_one.Run_game()
battlefield_one.display_welcome()

# Match Begins!

battlefield_one.battle_phase()

# Display the winner!

battlefield_one.display_winner()

