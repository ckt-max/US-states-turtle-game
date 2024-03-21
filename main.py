import pandas as pd
from turtle import Turtle, Screen
import time

from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 500)
screen.bgpic('blank_states_img.gif')
is_game_on = True

with open('50_states.csv') as file:
    data = pd.read_csv(file)

# turtle to write names:
pen = Turtle()
pen.hideturtle()
pen.penup()
state_list = data['state'].to_list()

# score:
score = Scoreboard()

guessed = 0
guessed_states = []

while guessed < 50:

    guess = screen.textinput('Guess the name of 50 US states','Enter name:').title()

    if guess in state_list:
        pen.goto(int(data[data.state == guess].x), int(data[data.state == guess].y))
        pen.write(guess, move=False, align='center',font=('Raleway', 8, 'normal'))
        score.update()
        guessed += 1
        guessed_states.append(guess)

    if guess == 'Exit':
        screen.bye()
        break

# states to learn
with open('states_to_learn.csv', mode='w+') as file:
    for state in state_list:
        if state not in guessed_states:
            file.write(state+'\n')



screen.exitonclick()