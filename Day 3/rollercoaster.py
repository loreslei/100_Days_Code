print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("Congratulations! You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if  18 <= age < 45:
        bill += 12
    elif age <= 12:
        bill += 5
    elif 45 <= age <= 55:
        print("Have a free ride on us.")
    else:
        bill += 7
    wants_photo = input("Do you want a photo? Y - Yes N - No\n")
    if wants_photo == "Y":
        bill += 3
    else:
        print("Alright!")
    print(f"Please pay ${bill}")
else:
    print("Sorry, you're too short to ride the rollercoaster.") 