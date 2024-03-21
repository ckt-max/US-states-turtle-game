from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0


        self.goto(300,-150)
        self.write(f'Score: {self.score}/50', move=False, align='center', font=('Raleway', 15, 'normal'))



    def update(self):
        self.clear()
        self.score += 1
        # self.write(f'Score: {self.score}', move=False, align='center', font=('Courier New', 15, 'normal'))
        self.goto(300,-150)
        self.write(f'Score: {self.score}/50', move=False, align='center', font=('Raleway', 15, 'normal'))
