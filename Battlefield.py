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

        con_bool = True
        while con_bool:
            user_input = input(f'Would you like to be Dinosaur: {self.dinosaur.name}? Y or N' '\n')
            if user_input == 'Y':
                print(f'You have chosen Dinosaur: {self.dinosaur.name}!' '\n')
                con_bool = False
            else:
                print(f'You have Chosen Robot: {self.robot.name}!' '\n')
                con_bool = False
            

        
        

    def battle_phase(self):
        input(f'What weapon would you like to use? Sword, Staff, or Hammer.')

        

        print(f'Now the match will begin!')
       

    def display_winner(self):
        self.winner = ()
