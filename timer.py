import time
from turtle import Turtle

class Timer(Turtle):

    def __init__(self, t):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(325, 200)
        self.start_time = t
        self.interval = 1

    def update(self):
        temp_time = time.time()
        while True:
            elapsed_time = time.time() - temp_time
            if elapsed_time > self.interval:
                self.clear()
                current_time = time.time()
                self.write(str(current_time - self.start_time), move=False, align='center', font=('Raleway', 15, 'bold'))