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
        
                    Hit "Enter" to begin''' '\n')

        con_bool = True
        while con_bool:
            user_input = input(f'Would you like to be Dinosaur: {self.dinosaur.name}? Y or N' '\n')
            if user_input == 'Y':
                print(f'You have chosen Dinosaur: {self.dinosaur.name}!' '\n')
                con_bool = False
            else:
                print(f'You have Chosen Robot: {self.robot.name}!' '\n')
                con_bool = False
            
        # input(f'What weapon would you like to use? Sword, Staff, or Hammer.')

        
        

    def battle_phase(self):
        print(f'''
        
                    Match is now starting... Get ready!''')  
        
       

        # attacking phase
        # create while loop, condition check while self.dino.health <= 0 or ...
        self.dinosaur.health = 100
        self.robot.health = 100
        while self.dinosaur.health or self.robot.health:
            
            self.dinosaur.attack(self.robot)
            print(f'{self.dinosaur.name} has attacked!')
            self.robot.attack(self.dinosaur)
            print(f'{self.robot.name} has responded with his own attack!')

            if self.robot.health <= 0:
                print(f'{self.dinosaur.name} health has been depleted!' '\n')
                break
            elif self.dinosaur.health <= 0:
                print(f'{self.dinosaur.name} health has been depleted!')
                break
            
            else:
                print(f'Here comes another attack sequence!')

    

    def display_winner(self):
        if self.dinosaur.health >= 1:
            print(f'{self.dinosaur.name} is the winner!')
        
        else:
            print(f'{self.robot.name} is the winner!')
