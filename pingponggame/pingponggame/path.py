import turtle
from turtle import Turtle,Screen


class pathSquare:
    trt = Turtle()
    def __init__(self):
        self.createSquarePath()

    def createSquarePath(self):
        self.trt.goto(-390,0)
        self.trt.shape("square")
        self.trt.color("red")
        self.trt.penup()
        self.trt.shapesize(0.8,5)
        self.trt.speed(30)

    def move_top(self):
        self.trt.setheading(90)
        self.trt.forward(3)

    def move_bottom(self):
        self.trt.setheading(270)
        self.trt.forward(3)

class pathSquare2:
    trt = Turtle()
    def __init__(self):
        self.createSquarePath2()

    def createSquarePath2(self):
        self.trt.goto(380,0)
        self.trt.shape("square")
        self.trt.color("red")
        self.trt.penup()
        self.trt.shapesize(0.8,5)
        self.trt.speed(30)

    def move_top2(self):
        self.trt.setheading(90)
        self.trt.forward(3)

    def move_bottom2(self):
        self.trt.setheading(270)
        self.trt.forward(3)


