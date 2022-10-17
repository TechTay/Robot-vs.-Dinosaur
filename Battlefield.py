from Robot import robot
from Dinosaur import dinosaur
from Weapon import weapon

class battlefield:
    

    def __init__(self):
        self.robot = robot()
        self.dinosaur = dinosaur()

    def Run_game(self):
        print(f'''
                    Game is starting...Please wait''' '\n')

        
        

    def display_welcome(self):
        print(f'''
                    Welcome to Robots vs. Dinosaurs!
                    Robot: {self.robot.name} vs. Dinosaur: {self.dinosaur.name}''')

        input(f'''
        
                    Type "Enter" to begin''' '\n')

        input(f'Who would you like to play as? The robot or dinosaur?' '\n')
        if dinosaur:
            print(f'You have chosen Dinosaur: {self.dinosaur.name}!' '\n')
        else:
            print(f'You have Chosen Robot: {self.robot.name}!' '\n')

        

        
        

    def battle_phase(self):
        input(f'What weapon would you like to use? Sword, Staff, or Hammer.')

        

        print(f'Now the match will begin!')
       

    def display_winner(self):
        self.winner = ()
