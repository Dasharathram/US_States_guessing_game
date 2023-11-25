import turtle
from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.setup(750, 500)
screen.title("U.S States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states_data = pd.read_csv("50_states.csv")
states_list = states_data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 Guessed states", prompt="What's another state's name?").capitalize()
    if answer == "Exit":
        break
    if answer in states_list:
        guessed_states.append(answer)
        t = Turtle()
        t.up()
        t.hideturtle()
        state_row = states_data[states_data.state == answer]
        t.goto(int(state_row.x.iloc[0]), int(state_row.y.iloc[0]))
        t.write(answer)
states_to_learn = []
#states to learn
for n in states_list:
    if n not in guessed_states:
        states_to_learn.append(n)
final_list = pd.DataFrame(states_to_learn)
final_list.to_csv("states_you_missed.csv")
