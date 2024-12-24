import random
from art import logo

def play_game(difficulty):
    
    random_number = random.randint(0,100)
    
    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5
        
    has_won = False
        
    for num in range(attempts):
        print(f"You have {attempts - num} attempts left to guess the number.") 
        guess = int(input("Make a guess: "))
        if(guess > random_number):
            print("Too high!")
            print("Guess again!")
        elif(guess == random_number):
            print("Congratulations! You guessed the number.")
            has_won = True
            break
        else:
            print("Too low!")
            print("Guess again!")
            
    if not has_won:
        print(f"You lost. The number was {random_number}.")    
        
        
        
print(logo[0])
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

level = input("Choose a difficulty. Type 'easy' or 'hard': \n").lower()
        
play_game(level)