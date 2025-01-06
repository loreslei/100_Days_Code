numbers = [1,2,3]

new_list = [n+1 for n in numbers]
#new_list = [new_item for item in list]
#new_list = [letter for letter in name]
#new_list = [new_item for item in list if test]
name = "Angela"
letters_list = [letter for letter in name]
range_list = [n*2 for n in range(1,5)]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
capital_names = [name.upper() for name in names if len(name) > 5]

print(capital_names)