print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill?\n$"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?\n"))
total_people = int(input("How many people to split the bill?\n"))

individual_value = (total_bill * (1 + tip/100)) / total_people

print("Each person should pay: $" + str(round(individual_value, 2)))