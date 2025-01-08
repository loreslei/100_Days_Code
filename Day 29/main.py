from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
RED = "#e7305b"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_random_password():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
        
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_to_file():
    web_name = website_entry.get()
    user = user_entry.get()
    password = pass_entry.get()
    info = f"Site: {web_name} | Email/Username: {user} | Password: {password}\n"
    
    
    size_web = len(web_name)
    size_user = len(user)
    size_pass = len(password)
    
    spaces_web = 0
    spaces_user = 0
    spaces_pass = 0
    
    
    #Validation web
    for symbol in web_name:
        if symbol == " ":
            spaces_web += 1
    
    if spaces_web == size_web:
        size_web = 0 
        
    #Validation user
    for symbol in user:
        if symbol == " ":
            spaces_user += 1
    
    if spaces_user == size_user:
        size_user = 0 
        
    #Validation password
    for symbol in password:
        if symbol == " ":
            spaces_pass += 1
    
    if spaces_pass == size_pass:
        size_pass = 0 
        
    if size_web != 0 and  size_user != 0 and size_pass != 0:
        is_ok = messagebox.askokcancel(title=web_name, message=f"These are the details entereded: \nEmail/Username:{user} \nPassword:{password} \nAre the informations correct?")
        if is_ok:
            with open("Day 29/save_pass.txt", mode="a") as file:
                website_entry.delete(0,END)
                pass_entry.delete(0,END)
                file.write(info)
    else:
        messagebox.showinfo(title="Missing Fields", message="Please do not leave any empty fields")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="Day 29/logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)


#First block

web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

#Second block

user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)

user_entry = Entry(width=35)
user_entry.insert(0, "example@gmail.com")
user_entry.grid(row=2, column=1, columnspan=2)

#Third block

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

pass_entry = Entry(width=17)
pass_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=generate_random_password)
generate_button.grid(row=3, column=2)

#Fourth block

add_btn = Button(text="Add", width=30, bg=RED, border=0, fg="white", command=add_to_file)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()