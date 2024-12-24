enemies = "Skeleton"


def increase_enemies():
    #global enemies --> how to change
    enemies += 1
    print(f"enemies inside function: {enemies}")
    
    
    
increase_enemies()
print(f"enemies outside function:{enemies}")