'''Turtle graphics, tuples and importing modules'''
import turtle as t
import random

tim=t.Turtle()
t.colormode(255) #we are making changes in the module 'turtle' not the obj Turtle()
tim.shape("turtle")
tim.color("dark violet") # https://www.tcl.tk/man/tcl8.4/TkCmd/colors.html
#Apple lisa one: first comp with GUI, before that we had terminal like eg:MS-DOS
#turtle relies on Tkinter 
# color guide: http://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html

'''Challenge: Draw a Square'''
# for i in range(0,4):
#     tim.forward(100)
#     tim.right(90)

'''Using aliases for module names'''
# import turtle as t
# from turtle import *
# from turtle import Turtle

'''Challenge: Draw a dashed line'''
# for i in range(0,15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

'''Challenge: A nested triangle, square, pentagon,...decagon'''
# colors=['dark sea green','dark green','firebrick','medium slate blue','coral']
# for n in range(3,11):
#     tim.color(random.choice(colors))
#     for i in range(0,n):
#         tim.forward(100)
#         tim.right(360/n)

'''Challenge: Random walk'''
# tim.pensize(10)
tim.speed("fastest")
directions=[0,90,180,270]
turtle_colors = ["black","blue","brown","cyan","darkblue","darkcyan","darkgreen","darkmagenta","darkorange","darkred","darkviolet","gold","green","indigo","lightblue","lightgreen","lime","magenta","maroon","navyblue","olive","orange","pink","purple","red",
"salmon","seagreen","sienna","skyblue","slateblue","springgreen","steelblue","tan","teal","turquoise","violet","white","yellow"
]


def random_color():
    r=random.randint(0,255)    
    g=random.randint(0,255)    
    b=random.randint(0,255)
    color=(r,g,b)
    return color
    

# for i in range(0,200):
#     #tim.color(random.choice(turtle_colors))
#     tim.color(random_color())
#     #tim.right(random.randint(0,360))
#     tim.setheading(random.choice(directions))
#     tim.forward(30)
    
    
'''Tuple: data type in python (1,2,3) each of the item in tuple are ordered'''
my_tuple=(1,2,3)
#tuple is immutable # use it when you don't want to accidently change items in it
#if you want to change: convert to list then change: list(my_tuple)
#my_tuple[2]=6 #error 


'''Challenge: Spirograph'''
def draw_spirograph(gap):
    for i in range(int(360/gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+gap)    
    

draw_spirograph(5)

screen=t.Screen()
screen.exitonclick()