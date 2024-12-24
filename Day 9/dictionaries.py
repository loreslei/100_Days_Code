programming_dicitonary ={
    "Python": "A high-level, interpreted programming language",
    "Java": "A general-purpose programming language",
    "C++": "A general-purpose programming language",
    "JavaScript": "An object-oriented programming language"
}

#print(programming_dicitonary["Java"])

programming_dicitonary["Loop"] = "Loop programming"

#print(programming_dicitonary)

empty_dicitonary = {}


# Wipe and existing_dicitonary

#programming_dicitonary = {}

#print(programming_dicitonary)

programming_dicitonary["Python"] = "Moth"

print(programming_dicitonary)


#Loop through a dictionary:
for key in programming_dicitonary:
    print(key)
    print(programming_dicitonary[key])