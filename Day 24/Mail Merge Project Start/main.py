#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
with open("Day 24/Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    names = file.readlines(64)
    
    
with open("Day 24\Mail Merge Project Start\Input\Letters\starting_letter.txt") as file:
    letter = file.readlines(100)
  
write_path = "Day 24/Mail Merge Project Start/Output/ReadyToSend"

for name in names:
    fixed_letter = ""
    fixed_name = name.strip()
    new_name = letter[0].replace("[name]",fixed_name)
    fixed_letter += new_name
    for line in range(1, len(letter)):
        fixed_letter += letter[line]
    with open(f"{write_path}/{fixed_name}_invitation", mode="w") as file:
        file.write(fixed_letter)
    
