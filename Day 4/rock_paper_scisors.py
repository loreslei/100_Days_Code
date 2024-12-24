import random


list_of_drawings = [
    '''
    
     _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    
    ''',
    '''
    
      _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    
    ''',
    '''
    
         _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    
    '''
]


choice = int(input("Type 0 - rock, 1 - scissors or 2 - paper\n"))

if 0 <= choice <= 2:
    print(f"You choose: \n {list_of_drawings[choice]}")

computer_choice = random.randint(0,2)
print(f"Computer choose: \n {list_of_drawings[computer_choice]}")

if(choice > 2):
    print(f"You typed an invalid number. You lose.")
elif choice == 0 and computer_choice == 1 or choice == 1 and computer_choice == 2 or choice == 2 and computer_choice == 0:
    print("You win!")
elif choice == computer_choice:
    print("It's a tie!")
else: 
    print("You lose!")