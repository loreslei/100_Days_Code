import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = NONE
reps = 0

FONT_CONFIG = (FONT_NAME, 35, "bold")
FONT_CONFIG_BUTTON = ("Arial", 16, "bold")

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    global reps
    window.after_cancel(timer)
    reps = 0
    timer = NONE
    timer_label.config(text="TIMER", fg=GREEN)
    check_label.config(text="")
    canvas.itemconfig(timer_text, text=f"00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    bell()
    if reps%8 == 0:
       count_down(long_break_sec)
       timer_label.config(text="LONG BREAK", fg=GREEN) 
    if reps%2 != 0:
        count_down(work_sec)
        timer_label.config(text="WORK",  fg=YELLOW) 
    else:
        count_down(short_break_sec)
        timer_label.config(text="BREAK",  fg=GREEN) 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# Bell function 
def bell(): 
    # call bell method 
    window.bell() 
  

def count_down(count):
    global timer
    minutes = int(count/60)
    seconds = count % 60
    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
#Window setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=PINK)

#Label Timer
timer_label = Label(text="TIMER",bg=PINK,font=FONT_CONFIG, fg=GREEN)
timer_label.grid(row=0, column=1)

#Image
canvas = Canvas(width=200,height=224, bg=PINK, highlightthickness=0)
tomato_img = PhotoImage(file="Day 28/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill=YELLOW, font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


#Button Start
button_start = Button(text="START", bg=RED, fg=YELLOW,font=FONT_CONFIG_BUTTON, border=0, command=start_timer)
button_start.grid(row=2, column=0)


#Label Check 
check_label = Label(font=FONT_CONFIG, fg=GREEN, bg=PINK)
check_label.grid(row=3, column=1)


#Button Reset
button_reset = Button(text="RESET", bg=RED, fg=YELLOW, font=FONT_CONFIG_BUTTON, border=0, command=reset)
button_reset.grid(row=2, column=2)

window.mainloop()