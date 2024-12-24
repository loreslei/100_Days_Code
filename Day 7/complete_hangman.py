import random
from hangman_art import hangman
from hangman_art import logo
from hangman_words import word_list


random_word = random.choice(word_list)

word_size = len(random_word)

word = ""

guessing_word = []

print(logo[0])

for letter in range(word_size):
    word += "_"
    guessing_word.append("_")
    
print(f"word: {word}")


end = False

counter = 0

life = 6

print(hangman[(life * -1) -1])


while not end:
    
    print(f"\nYou have {life} life(s) remaining")
    
    guess = input("\nGuess a letter: ").lower()
    
    if guess in guessing_word:
        print(f"You've already guessed {guess}!")
    
    for letter in range(word_size):
        if guess == random_word[letter]:
            guessing_word[letter] = guess
            counter += 1
                   
    if guess not in random_word:
        life -= 1
        print(f"The letter {guess} does not exist in the word.")
                
    word = ""
    
    for letter in guessing_word:
        word += letter
    
    print(f"\nword: {word}")  
      
    print(hangman[(life * -1) -1])
    

    if counter == word_size:
        end = True
        print(f"You've won! The word was: {random_word}")
        
    if life == 0:
        end = True
        print(f"You've lost! The word was: {random_word}") 
      

        
 