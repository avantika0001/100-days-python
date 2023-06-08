#making classes

# class User:
#     pass #we can leave the class content empty dor now by using the keyword #"pass"

# class User:
#     pass

# user_1= User()
'''Making objects like this is prone to error'''
# user_1.id="001"
# user_1.username="avantika"
# user_2= User()
# user_2.id="001"
# user_2.name="avantika"

'''constructor'''
#initializing an object,it's variables witha astarting values 

class User:
    def __init__(self,user_id,username): #geyts called everytime we create a new object from this class
        #print("new user being creater...")
        #when we add parameters to constructor, we must provide these 2 attributes while making an obj now
        self.id=user_id #setting the attribute of the obj
        self.username=username
        self.followers=0 #we can give a default value to an attribute
        self.following=0
    def follow(self, user):
        self.followers += 1 #'self':refer to obj created by the class
        self.following += 1    

user_1= User("001","avantika")
#user_2= User("001") #error
user_2=User("002","anushka")
user_1.follow(user_2)
print(user_1.followers)       
        


