from turtle import Turtle, Screen
# from turtle import Screen
import random


tommy =  Turtle()
tommy.shape("turtle")
tommy.turtlesize(3)
tommy.pensize(8)

# opakování něčeho podtím 4x (0,1,2,3)

# for numb in range(0,10):
#     tommy.forward(100)
#     tommy.right(90)

# přerušovaná čára

# for _ in range(0,8):
#     tommy.pendown()
#     tommy.forward(20)
#     tommy.penup()
#     tommy.forward(20)


# tommy.forward(200)
# tommy.speed(5)
# tommy.right(90)
# tommy.pencolor("blue")
# tommy.pensize(30)
# tommy.forward(200)
# tommy.right(90)
# tommy.pensize(50)
# tommy.circle(25)
# tommy.right(90)

# PRÁCE S NÁHODOU

colors = ["red", "blue", "pink", "violet", "green", "yellow"]
rotation = [0, 90, 180, 270]
for _ in range(200):

# náhodný výběr barvy

    random_color = random.choice(colors)
    tommy.pencolor(random_color)

# pohyb

    tommy.forward(30)
    tommy.right(random.choice(rotation))












my_screen = Screen()
my_screen.exitonclick()

