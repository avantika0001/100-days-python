#OOP

#procedural programming: increasing complexity and no. of relationships to manage
#to maintain a simpls relatioship in project while writing more and more complex projects
#break large task to smaller reusable bits

#objects: they have a piece of data/property:attribute, they have things they can do/functionalities:methods

#blueprint: class, the actual object created:object

# import another_module
# print(another_module.another_variable)

# import turtle
# #https://docs.python.org/3/library/turtle.html

# timmy=turtle.Turtle() #we importes Turtle() class from turtle module
# # print(turtle)
# timmy.shape("circle")
# timmy.color("coral")
# timmy.forward(100) 

# #object.attribute
# my_screen=turtle.Screen()
# print(my_screen.canvheight) #my_screen: object; canvheight:attribute

# #object.method()
# my_screen.exitonclick()

#module: each file we create in project is module in itself
#package: a whole bunch of code, lots of files together

#https://pypi.org/

#pip install prettytable

from prettytable import PrettyTable

table=PrettyTable()

table.add_column("Pokemon name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
print(table.align)
table.align="l"
print(table)










