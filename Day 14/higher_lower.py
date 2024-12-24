import random
from art import logo
#from data import instagram
from data_2 import instagram

def compare(profile1, profile2, higher):
    count1 = profile1["follower_count"]
    count2 = profile2["follower_count"]
    
    winner = 0
    lost = 0
    
    if count1 > count2:
        winner = count1
        lost = count2
    else:
        winner = count2
        lost = count1
    
    if higher == 1 and count1 > count2:
        print("You won!")
        
    elif higher == 2 and count2 > count1:
        print("You won!")
    else:
        print(f"You lost! The other profile had {winner} followers while your choice had {lost} followers.")
        return False
        
    return True
        
def play_game(list, game_logo):        

    print(game_logo[0])
    
    restart = True
    
    gaming = True
    
    while restart:
        profiles = []
        print(len(profiles))
        
        while gaming:
            
            random_profile1 = random.choice(list)
            random_profile2 = random.choice(list)
            
            while random_profile1 == random_profile2:
                random_profile2 = random.choice(list)
            
            profiles.append(random_profile1)
            profiles.append(random_profile2)
            
            print(f"{random_profile1["name"]} a {random_profile1["description"]} from {random_profile1["country"]}")
            print(game_logo[1])
            print(f"{random_profile2["name"]} a {random_profile2["description"]} from {random_profile2["country"]}")
            choice = int(input("Choose the one you think has the most followers on instagram!\nType '1' if you think it is the first one, type '2' if you think it is the second one: "))
            
            if not compare(random_profile1, random_profile2, choice):
                break
            
            
        again = input("Wanna try again? type (y/n): ").lower()
        if again == "n":
            restart = False
            print("Goodbye!")
        else:
            print("\n" * 100)



play_game(instagram, logo)
    
        
        
        
