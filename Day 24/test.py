file = open("Day 24\my_file.txt", mode="a") #mode a or w
#with open("Day 24\my_file.txt") as file: - Does not need to close the file
file.write("\nte nandayo")

file.close()



with open("Day 24\my_file.txt", mode="w") as file:
    file.write("Hehehe (✿◡‿◡)")