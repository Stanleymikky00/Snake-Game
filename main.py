#from turtle import Turtle, Screen
#3.it was initially written as its written on the top comment, but for error reasons we have to remove the
#Turtle. but when writting a new snake game start with the import turtle.
from turtle import Screen

#NOTE WE HAD TO IMPORT THE SNAKE FILE FROM THE SNAKE MODULE
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
from data_recorder import save_data
from agent import choose_action

#IMPORTANT SWITCH BETWEEN AI AGENT AND HUMAN
USE_AI = True  # Switch between human or AI control


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#3.FOODCLASS: HERE WE'RE BRINGING THE FOOD CLASS

snake = Snake()
food = Food()
scoreboard = Scoreboard()

#this function is associated with the AI agent integration to this game
def get_game_state(snake, food):
    head = snake.head
    state = {
        "head_x": head.xcor(),
        "head_y": head.ycor(),
        "food_x": food.xcor(),
        "food_y": food.ycor(),
        "direction": snake.direction
    }
    return state


#this allow us to track the movement of our game so we have to creat this function
def move_up():
    snake.up()
    state = get_game_state(snake, food)
    save_data(state, "Up")

def move_down():
    snake.down()
    state = get_game_state(snake, food)
    save_data(state, "Down")

def move_left():
    snake.left()
    state = get_game_state(snake, food)
    save_data(state, "Left")

def move_right():
    snake.right()
    state = get_game_state(snake, food)
    save_data(state, "Right")


#CREATING THE KEY LISTEN METHOD
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

#while runing our code from line 39 we noticed that the snake was not going the together
#so in order to make them go together we introduced the tracer method by turning it off by 0


#background color


#ALSO HERE WE HAVE TO CREAT A NEW SNAKE OBJECT


#creating the snake body
#segment_1 = Turtle()
#segment_1.shape("square")
#segment_1.color("white")

#segment_2 = Turtle()
#segment_2.shape("square")
#segment_2.color("white")
#segment_2.goto(x=-20,y=0)

#segment_3 = Turtle()
#segment_3.shape("square")
#segment_3.color("white")
#segment_3.goto(x=-40, y= 0)


#starting_position = (0,0),(-20,0),(-40,0)
segments = []

# using for loop to creat position
#for position in starting_position:
#new_segment = Turtle()
#new_segment.shape("square")
#new_segment.color("white")
#new_segment.penup()
#new_segment.goto(position)
#segments.append(new_segment)
#ALL THIS WAS MOVED TO SNAKE.PY (SEARCH FOR SAME CODE)


# so here we decided to call the tracer we introduced in lin 8 by calling update.
# the reason for this is for all the segment to run together


#moving the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #AI AGENT LOOP
    if USE_AI:
        state = get_game_state(snake, food)
        action = choose_action(state)

        if action == "Up":
            snake.up()
        elif action == "Down":
            snake.down()
        elif action == "Left":
            snake.left()
        elif action == "Right":
            snake.right()

    #3. DETECTING COLLISION WITH FOOD
    #4. KEEPING TRACK WITH THE SCORE WHEN THE SNAKE COLLIDE WITH THE FOOD
    #we used 15 cause the food size is 10 by 10
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #DETECT COLLISION WITH WALL:
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        #scoreboard.reset()
        game_is_on = False
        scoreboard.game_over()

    #DEETCT COLLISION WITH TAIL: (we will be using the slicing method)
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            game_is_on = False
            scoreboard.game_over()

    #for segment in snake.segments:
        #if segment == snake.head:
        #pass
        #elif snake.head.distance(segment) < 10:
        #game_is_on = False
        #scoreboard.game_over()

    #for seg_num in range(len(segments) -1, 0, -1):
    #   new_x = segments[seg_num -1].xcor()
    #  new_y = segments[seg_num -1].ycor()
    # segments[seg_num].goto(new_x, new_y)

    #NOTE: THIS CODE WAS ALSO MOVED TO SNAKE.PY (SEARCH FOR THE CODE IN SNAKE.PY)
    #NOTE: IN SNAKE.PY THE SEGMENTS TOOK A NEW CODE CALLED SELF.SEGMENT

#NOTE:THE COMMENT ON CAPITAL LETTER WERE WRITTEN AFTER SNAKE.PY WAS CREATED


screen.exitonclick()
