from turtle import Turtle

class bouncing_ball:
    trt = Turtle()
    def __init__(self):
        self.ball_shape()

    def ball_shape(self):
        self.trt.shape("circle")
        self.trt.goto(0,0)
        self.trt.shapesize(1)
        self.trt.penup()
        self.trt.color("white")

