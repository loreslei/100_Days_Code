import random

word_list = ["bamboo", "camel", "caramel"]

random_word = random.choice(word_list)
print(random_word)

guess = input("Guess a letter: ").lower()

for letter in random_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")