import random

word_list = ["bamboo", "camel", "caramel"]

random_word = random.choice(word_list)
print(random_word)


word_size = len(random_word)

word = ""

guessing_word = []

for letter in range(word_size):
    word += "_"
    guessing_word.append("_")
    
print(f"{word}")


won = False

counter = 0

while not won:
    
    guess = input("Guess a letter: ").lower()
    
    for letter in range(word_size):
        if guess == random_word[letter]:
            guessing_word[letter] = guess
            counter += 1
            
    word = ""
    
    for letter in guessing_word:
        word += letter
    
    print(f"After guess: {word}")    

    if counter == word_size:
        won = True
        print(f"You've won! The word was: {random_word}")
        

        
 