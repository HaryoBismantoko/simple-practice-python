import turtle
from turtle import Turtle,Screen
import tkinter as tk

scr = Screen()
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class snake:
    def __init__(self):
        self.scr = Screen()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def screen_game(self):
        self.scr.setup(width=600, height=600)
        # self.scr.screensize(600,600)
        self.scr.bgcolor("black")
        self.scr.title("GAME ULER")
        self.scr.tracer(0)
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.ext_snake(position)
    def ext_snake(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def add_snake(self):
        self.ext_snake(self.segments[-1].position())
    def move_forward(self):
        for seg_num in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    def movement(self):
        self.scr.listen()  # input keyboard arrow
        self.scr.onkeypress(self.turn_left, 'Right')
        self.scr.onkeypress(self.turn_left, 'd')
        self.scr.onkeypress(self.turn_right, 'Left')
        self.scr.onkeypress(self.turn_right, 'a')
        self.scr.onkeypress(self.turn_forward, 'Up')
        self.scr.onkeypress(self.turn_forward, 'w')
        self.scr.onkeypress(self.turn_backward, 'Down')
        self.scr.onkeypress(self.turn_backward, 's')
        # self.scr.mainloop()  # untuk stay diprogram yang berjalan
    def turn_left(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    def turn_right(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def turn_forward(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def turn_backward(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    # def move_forward(self):
    #     self.turtle.penup()
    #     self.turtle.forward(20)  # Atur berapa langkah snake bergerak maju
    #     self. scr.ontimer(self.move_forward, 100)  # Panggil kembali fungsi setiap 100 milidetik
