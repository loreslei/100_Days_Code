import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Day 25/us-game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


answer_state = screen.textinput(title="Guess the State", prompt="What's another states's name?")


screen.exitonclick()
""" def get_mouse_click_cor(x, y):
    print(x, y)
    
turtle.onscreenclick(get_mouse_click_cor)    
turtle.mainloop() """