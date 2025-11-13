# A Rock Paper Scissors game where the user plays against the computer, with a menu, game logic, and score tracking.

import random

class Game:
    play_options = ['rock','paper', 'scissors']
    decision_dict = {'rock': 'scissors', 
                     'scissors': 'paper', 
                     'paper': 'rock' 
                     }
    def __init__(self):
       pass
    
    def get_user_item(self):
        while True:
            user_input = input("Enter one of rock/paper/scissors: ")
            if user_input not in Game.play_options:
                print("Word is not Valid please try again")
                continue
            else:
                return user_input
    
    def get_computer_item(self):
        return random.choice(Game.play_options)
    
    def get_game_result(self, user_item, computer_item):
        if Game.decision_dict[user_item] == computer_item:
            return 'win'
        elif Game.decision_dict[computer_item] == user_item:
            return 'loss'
        else:
            return 'draw'
        
    def play(self):    
        u_item = self.get_user_item()
        c_item = self.get_computer_item()
        result = self.get_game_result(u_item,c_item)
        print(f"OutCome the game is {result}, user choice is {u_item}, computer choice is {c_item}")
        return result      
    