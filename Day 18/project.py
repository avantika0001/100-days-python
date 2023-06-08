'''Damien Hirst : spot painting'''

import colorgram
import turtle as t
import random

# rgb_colors=[]
# colors = colorgram.extract('spotpaint.jpg', 30)
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     rgb_colors.append((r,g,b))
    
#print(rgb_colors)    
color_extracted=[(249, 248, 244), (250, 245, 248), (243, 250, 246), (236, 244, 250), (236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34)]

tim=t.Turtle()
t.colormode(255)

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for i in range(1,100):
        [tim.dot(10,random.choice(color_extracted))
        tim.penup()
        tim.forward(50)
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)       

    
screen=t.Screen()
screen.exitonclick()    
   #,random.randint(0,len(color_extracted)) 
