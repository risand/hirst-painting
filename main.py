import turtle as turtle_module
import random
color_list = [(138, 167, 197), (196, 139, 149), (210, 153, 116), (26, 37, 56), (54, 105, 143), (145, 179, 163), (155, 66, 55), (231, 213, 103), (137, 66, 74), (151, 28, 34), (50, 38, 43), (29, 53, 48), (55, 109, 90), (229, 167, 172), (151, 30, 27), (203, 86, 75), (189, 98, 107), (49, 42, 38), (231, 171, 162), (19, 93, 70), (175, 190, 214), (110, 123, 158), (27, 61, 109), (173, 202, 190), (51, 149, 193), (64, 67, 55)]

tim = turtle_module.Turtle()
tim.hideturtle()
tim.speed("fastest")
turtle_module.colormode(255)

tim.penup()
y = -180

for _ in range(10):
    tim.setx(-220)
    tim.sety(y)
    y += 50
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)




screen = turtle_module.Screen()
screen.exitonclick()
