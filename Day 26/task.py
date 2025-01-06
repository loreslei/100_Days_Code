import pandas
#Review this lesson
#Create a dict in this format {"A":"Alfa", "B":"Bravo"}
path = "Day 26/NATO-alphabet-start/nato_phonetic_alphabet.csv"
data = pandas.read_csv(path)
phonetic_dict = {row.letter:row.code for(index,row) in data.iterrows()}
print(phonetic_dict)

#Create a list of the phonetic code words from a word that the user inputs
word = input("Enter a word:\n").upper()
spell = [phonetic_dict[letter] for letter in word]
print(spell)