import turtle
import pandas
from text import Text

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Day 25/us-game/blank_states_img.gif"
screen.addshape(image)
screen.setup(width=725, height=491)
turtle.shape(image)

guessed_correctly = 0

data = pandas.read_csv("Day 25/us-game/50_states.csv")
states_list = data["state"]
guessed_states = []

score = Text(-300, 200, f"{guessed_correctly}/50")
while guessed_correctly != 50:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another states's name?").lower()
    if answer_state == "exit":
        missing_states = []
        for state in states_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_csv = pandas.DataFrame(missing_states)
        new_csv.to_csv("Day 25/us-game/states_to_study.csv")
        break
    for state in states_list:
        if answer_state == state.lower():
            row = data[data["state"] == state]
            x =  int(row.x.iloc[0])
            y =  int(row.y.iloc[0])
            text = Text(x, y, state)
            guessed_correctly += 1
            guessed_states.append(state)
    score.update_score(f"{guessed_correctly}/50")

if guessed_correctly == 50:    
    win = Text(0, 0, "You win!")   

screen.exitonclick()


""" def get_mouse_click_cor(x, y):
    print(x, y)
    
turtle.onscreenclick(get_mouse_click_cor)    
turtle.mainloop() """