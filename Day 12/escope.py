game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]


def create_enemy():
    new_enemy = ""
    if game_level == 1:
        new_enemy = enemies[0]
    print(new_enemy)

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")
    
    
increase_enemies()
print(f"enemies outside function: {enemies}")

def drink_potion():
    potion_strength = 2
    print(potion_strength)
    
drink_potion()