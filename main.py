from turtle import Turtle ,Screen
import random
import turtle

rocky = Turtle()
turtle.colormode(255)
rocky.shape("turtle")
rocky.color("coral")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
rocky.speed(10)
rocky.pensize(2)
direction = [0, 90, 180, 270]

# for _ in range(0,4):
#     rocky.forward(100)
#     rocky.right(90)

# for _ in range(15):
#     rocky.forward(10)
#     rocky.pencolor("white")
#     rocky.forward(10)
#     rocky.pencolor("black")


# def shape(side):
#     shape_angle = 360 / side
#     for _ in range(side):
#         rocky.forward(100)
#         rocky.right(shape_angle)
#     rocky.color(random.choice(colours))
#
# for times in range(3,11):
#     shape(times)

# def random_walk():
#     rocky.pensize(10)
#     rocky.forward(random.randint(1,150))
#     rocky.backward(random.randint(1, 150))
#     rocky.left(random.randint(1, 150))
#     rocky.right(random.randint(1, 150))
#     rocky.color(random.choice(colours))
# for _ in range(50):
#     random_walk()

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)
#
# def spirograph(gap):
#     for _ in range(int(360/gap)):
#     # rocky.forward(30)
#     # rocky.setheading(random.choice(direction))
#         rocky.circle(50)
#         rocky.setheading(rocky.heading()+10)
#         rocky.color(random_color())
#
# spirograph(5)
color_list = [ (41, 104, 174), (234, 205, 114), (228, 151, 85), (189, 46, 74), (231, 118, 144), (115, 90, 46),
               (110, 107, 189), (216, 60, 77), (114, 186, 136), (122, 176, 212), (52, 178, 110), (204, 16, 40),
               (115, 171, 36), (223, 57, 47), (31, 58, 117), (154, 223, 195), (182, 168, 223), (23, 142, 107),
               (29, 164, 172), (85, 35, 37), (39, 45, 84), (229, 169, 182), (232, 174, 161), (81, 39, 38),
               (151, 206, 223), (92, 43, 42)]

rocky.penup()
rocky.setheading(205)
rocky.forward(800)
rocky.setheading(0)

for dots in range(1,101):
    rocky.dot(20, random.choice(color_list))
    rocky.forward(100)
    if dots % 10 == 0:
        rocky.setheading(90)
        rocky.forward(50)
        rocky.left(90)
        rocky.forward(1000)
        rocky.setheading(0)





screen = Screen()
screen.exitonclick()