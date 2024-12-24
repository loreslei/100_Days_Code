import random

word_list = ["bamboo", "camel", "caramel"]

random_word = random.choice(word_list)
print(random_word)


word_size = len(random_word)

word = ""

for letter in range(word_size):
    word += "_"
    
print(f"{word}")

guess = input("Guess a letter: ").lower()

display = ""

for letter in random_word:
    if guess == letter:
        display += letter
    else:
        display += "_"


print(f"After guess: {display}")
        

        
