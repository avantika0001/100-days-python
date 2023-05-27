#scope: eg: apple tree in home vs. in neighbourhood

# apple=2 #global scope
# def apple_num():
#     apple=4
#     banana=4
#     print(f"apples you have access to inside function: {apple}")
# apple_num()
# #print(banana) ##'banana' has local scope ;can be accessed only inside the block in which it's declared
# print(f"apples you have access to outside function: {apple}") ##'apple has global scope'

##Namespace: first time where you write that line of code(declaring a varibale or function) defines the scope of that particular variable/function

#In Python there is NO block scope(if while for blocks don't create local scope)
#separate local scope only created when we use functions

# level=6
# enemies=['a','b','c']
# if level>3:
#     new_enemey='e'
# print(new_enemey) #valid
# def play():   
#     enemies=['a','b','c']
#     if level>3:
#         new_enemey1='e'
# print(new_enemey1) #Notvalid as function has created a local scope  

##Modifying Global Scope

enemies=1

def increase_enemies():
    # global enemies
    # enemies+=1
    print(f"Enemies inside the function: {enemies}")
    return enemies+1 #better way of doing it

#increase_enemies()
enemies = increase_enemies()
print(f"Enemies outside the function: {enemies}")

#global constants
PI=3.141
URL="http://www.google.com"
#writing the variable name in all uppercase means we are never going to modify its value in our code
