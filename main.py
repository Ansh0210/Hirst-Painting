# import colorgram
#
# rgb_list = []
#
# colors = colorgram.extract('image.jpg', 25)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_list.append((r, g, b))
#
# print(rgb_list)

import turtle as t
import random as rand

rgb_list = [(236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
            (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165),
            (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
            (147, 17, 19)]

tim = t.Turtle()
t.colormode(255)
tim.speed("fast")


def draw_horizontal_dots(num_of_dots):
    for _ in range(num_of_dots):
        tim.dot(20, rand.choice(rgb_list))
        tim.pu()
        tim.forward(50)


tim.hideturtle()
start_x, start_y = -200, -200
tim.teleport(start_x, start_y) # initial position for the dot to be drawn

for _ in range(10):
    draw_horizontal_dots(10) # draw 10 dots horizontally
    start_y += 50 # increase y position by 50
    tim.teleport(start_x, start_y) # teleport to new position


screen = t.Screen()
screen.exitonclick()

