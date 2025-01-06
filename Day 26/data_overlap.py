
with open("Day 26/file1.txt") as file1:
    numbers1 =  file1.readlines()
    numbers1 = [int(number.strip()) for number in numbers1]


with open("Day 26/file2.txt") as file2:
    numbers2 =  file2.readlines()
    numbers2 = [int(number.strip()) for number in numbers2]
    

result = [number for number in numbers1 if number in numbers2]

print(result)