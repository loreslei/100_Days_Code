def calculate_love_score(name1, name2):
    counterTrue = 0
    counterLove = 0
    
    name1lower = name1.lower()
    name2lower = name2.lower()
    
    for letter in name1lower:
        if letter in "true":
            counterTrue += 1
        if letter in "love":
            counterLove += 1
    for letter in name2lower:
        if letter in "true":
            counterTrue += 1
        if letter in "love":
            counterLove += 1
    
    print(f"{counterTrue}{counterLove}")
    
    
calculate_love_score("Kanye West", "Kim Kardashian")