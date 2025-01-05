import pandas

path = "Day 25/data_squirrel.csv"

data = pandas.read_csv(path)

# how many gray, black or cinnamons

#My solution
fur = data["Primary Fur Color"]
gray = fur == "Gray"
cinna = fur == "Cinnamon"
black = fur == "Black"
counter_gray = 0
counter_cinna = 0
counter_black = 0

for i in gray:
    if i == True:
        counter_gray+=1
for i in cinna:
    if i == True:
        counter_cinna+=1
for i in black:
    if i == True:
        counter_black+=1
        
        
my_dict = {
    "Fur Color":["Gray", "Cinnamon", "Black"],
    "Count": [counter_gray, counter_cinna, counter_black]
}

print(my_dict)

new_data = pandas.DataFrame(my_dict)

new_data.to_csv("Day 25/fur_color.csv")


#Angela's

gray = len(data[data["Primary Fur Color"]  == "Gray"])
cinna = len(data[data["Primary Fur Color"]  == "Cinnamon"])
black = len(data[data["Primary Fur Color"]  == "Black"])

data_dict = {
    "Fur Color":["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinna, black]
}

new_data = pandas.DataFrame(data_dict)

new_data.to_csv("Day 25/fur_color.csv")