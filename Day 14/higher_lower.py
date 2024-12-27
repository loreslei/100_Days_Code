import random
from art import logo
from data import instagram

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
        index2 = 0
        indexof2 = 0
        
        print(game_logo[0])
        
        while gaming:
            
            
            if counter == 0:
               random_profile1 = random.choice(list)
                 
               
            random_profile2 = random.choice(list)
            indexof2 = list.index(random_profile2)
            
            while random_profile1 == random_profile2 or indexof2 == index2:
                random_profile2 = random.choice(list)
            
            
            acc1_name = random_profile1["name"]
            acc1_desc = random_profile1["description"]
            acc1_cont = random_profile1["country"]
            
            acc2_name = random_profile2["name"]
            acc2_desc = random_profile2["description"]
            acc2_cont = random_profile2["country"]
            
            
            
            print(f"\n{acc1_name} a {acc1_desc} from {acc1_cont}\n")
            print(game_logo[1])
            print(f"\n{acc2_name} a {acc2_desc} from {acc2_cont}\n")
            
            try:
                choice = int(input("\nChoose the one you think has the most followers on instagram!\nType '1' if you think it is the first one, type '2' if you think it is the second one: "))
            except ValueError:
                print("\nYou must type an number between 1 or 2, please try again.\n")
                choice = int(input("\nChoose the one you think has the most followers on instagram!\nType '1' if you think it is the first one, type '2' if you think it is the second one: "))
                
            if not compare(random_profile1, random_profile2, choice):
                break
            
            else:
                if choice == 2:
                    random_profile1 = random_profile2
                else:
                    index2 = list.index(random_profile2)
                counter += 1
                print(f"\nYour score: {counter}\n")
            
            
        again = input("\nWanna try again? type (y/n): ").lower()
        if again == "n":
            restart = False
            print("\nGoodbye!")
        else:
            print("\n" * 100)



play_game(instagram, logo)
    

        
        
        
