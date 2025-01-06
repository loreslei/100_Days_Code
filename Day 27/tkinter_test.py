from tkinter import *
import turtle
window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)
def button_clicked():
    string = input.get()
    my_label.config(text=f"{string}")
    
#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
#my_label.pack(expand=True)
#my_label.pack()
#my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
#Ways of changing text
my_label["text"] = "New Text"
my_label.config(text="New Text")
#tim = turtle.Turtle()

#Button

button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="New Button", command=button_clicked)
button2.grid(column=2, row=0)

#Entry
input = Entry()
input.grid(column=3, row=2)
input.get()


window.mainloop()