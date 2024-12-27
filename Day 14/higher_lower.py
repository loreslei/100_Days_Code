import random
from art import logo
from data import instagram


def format_account(profile, id):
    acc_name = profile["name"]
    acc_desc = profile["description"]
    acc_cont = profile["country"]
    acc_followers = profile["follower_count"]
    
    if id == 1:
        print(f"\n{acc_name} a {acc_desc} from {acc_cont} that has {acc_followers} followers\n")
    else:
        print(f"\n{acc_name} a {acc_desc} from {acc_cont}\n")

    

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
        print("\nYou won!\n")
        
    elif higher == 2 and count2 > count1:
        print("\nYou won!\n")
    else:
        print(f"\nYou lost! The other profile had {winner} followers while your choice had {lost} followers.\n")
        return False
        
    return True
        
def play_game(list, game_logo):        

    
    restart = True
    
    gaming = True
    
    
    while restart:
        
        counter = 0
        
        print(game_logo[0])
        
        while gaming:
            
            
            if counter == 0:
               random_profile1 = random.choice(list)
            else:
                random_profile1 = random_profile2     
               
            random_profile2 = random.choice(list)
            
            while random_profile1 == random_profile2:
                random_profile2 = random.choice(list)
                
            format_account(random_profile1, 1)
            print(game_logo[1])
            format_account(random_profile2, 2)
            
            
            try:
                choice = int(input("\nChoose the one you think has the most followers on instagram!\nType '1' if you think it is the first one, type '2' if you think it is the second one: "))
            except ValueError:
                print("\nYou must type an number between 1 or 2, please try again.\n")
                choice = int(input("\nChoose the one you think has the most followers on instagram!\nType '1' if you think it is the first one, type '2' if you think it is the second one: "))
                
            if not compare(random_profile1, random_profile2, choice):
                break
            else:
                counter += 1
            
            print(f"\nYour score: {counter}\n")
            
        print(f"\nYour final score: {counter}\n")
            
        again = input("\nWanna try again? type (y/n): ").lower()
        if again == "n":
            restart = False
            print("\nGoodbye!")
        else:
            print("\n" * 100)



play_game(instagram, logo)
    

        
        
        
