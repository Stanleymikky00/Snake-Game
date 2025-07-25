#starting position was taken from the main.py and its called constant
#and in python the constant are all in capital letters

# Note: we also use self when we are working a class
from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        #THIS WAS CREATED TO LINK THE KEY PRESS
        self.head = self.segments[0]
        self.direction = "Right"

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
            #new_segment = Turtle()
            #new_segment.shape("square")
            #new_segment.color("white")
            #new_segment.penup()
            #new_segment.goto(position)
            #self.segments.append(new_segment)

    #4. CREATING A FUNCTION THAT EXTENDS THE SNAKE LENGTH:
    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        #self.head.setheading(90)
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.direction = "Up"

    def down(self):
        #self.head.setheading(270)
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.direction = "Down"

    def left(self):
        #self.head.setheading(180)
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.direction = "Left"

    def right(self):
        #self.head.setheading(0)
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.direction = "Right"
