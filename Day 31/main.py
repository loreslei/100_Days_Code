from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
FONT_BOLD =  ("Arial", 40, "bold")
FONT_ITALIC =  ("Arial", 60, "italic")

try:
    DATA = pandas.read_csv("Day 31/data/words_to_learn.csv")
except FileNotFoundError:
    DATA = pandas.read_csv("Day 31/data/french_words.csv")
      
to_learn = pandas.DataFrame.to_dict(DATA, orient="records")


current_card = {}


#Generate words
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    word_fr = current_card["French"]
    canvas.itemconfig(canvas_title, text="French", fill="black")
    canvas.itemconfig(canvas_word, text=word_fr, fill="black")
    canvas.itemconfig(canvas_image, image=front_img)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    word_en = current_card["English"]
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=word_en, fill="white")
    canvas.itemconfig(canvas_image, image=back_img)
    
def right_button():
    print(len(to_learn))
    to_learn.remove(current_card)
    new_csv = pandas.DataFrame(to_learn)
    new_csv.to_csv("Day 31/data/words_to_learn.csv", index=False)
    next_card()    


#UI

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="Day 31/images/card_front.png")
back_img = PhotoImage(file="Day 31/images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
canvas_title = canvas.create_text(400, 150, text="", font=FONT_ITALIC)
canvas_word = canvas.create_text(400, 263, text="", font=FONT_BOLD)

canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="Day 31/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, border=0, command=right_button)
right_button.grid(column=1, row=1)
wrong_image = PhotoImage(file="Day 31/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, border=0, command= next_card)
wrong_button.grid(column=0, row=1)




next_card()

window.mainloop()