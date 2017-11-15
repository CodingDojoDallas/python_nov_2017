# class User(object):
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.logged = True
#     def login(self):
#         self.logged = True
#         print self.name + " is logged in."
#         return self
#     def logout(self):
#         self.logged = False
#         print self.name + " is not logged in"
#         return self
#     def show(self):
#         print "My name is {}. You can email me at {}".format(self.name, self.email)
#         return self

# class User(object):
#     pass

#When i define one parameter to be object, it just means that this class 
#inherits from the object class.
#The pass is a placeholder when code is required. It means do nothing.

# class ClassName(object):
  #attributes and methods here (we'll talk more about these in a moment)

#A class is a blueprint for creating something. Once the blueprint is finished then we create
#instances of the class. We create a new instance by using the class name as a function.

# erbold=User()
# anna=User()

# print erbold, anna

#A class is the blueprint and the object as the thing we make based on the blueprint.
#Objects have two important parts: storage of information and ability to execute some logic. 
#Objects can store two different types of information: attributes and methods. Attributes are
#characteristics of an object and methods are things an object can do. 

# declare a class and give it name User
# class User(object):
#     # the __init__ method is called every time a new object is created
#     def __init__(self, name, email):
#         # set some instance variables. just like any variable we can call these anything
#         self.name = name
#         self.email = email
#         self.logged = False
#     # this is a method we created to help a user login
#     def login(self):
#         self.logged = True
#         print self.name + " is logged in."
#         return self
# #now create an instance of the class
# new_user = User("Anna","anna@anna.com")
# print new_user.email


#The _init_method is called every time a new object is created. 
#New object creation includes passing parameters.
#Anything passed in here is passed into the init method: new_user=User("Anna", "anna@anna.com")
#Now setting some values that belong to each object to be equal to the values we passed in:
#self.email=email
#Another method besides the init method is called login. All it does for now is print a string.
#The logic to log a user into a web app is pretty complicated. It requires a database. We'll be
#be writing the code for that later on in Flask.
#To review any method/function that is included in the parent class definition can be called
#by an object of that class.

#The first parameter in our method/function was "self": def login(self,id): - It's true for
#any method that we create.
#However when we call methods we do not have to pass in any arguments. It's called implicit passage
#of self. We can now change the state of the single object by making modifications only to self.
#What??
#The self parameter includes all the information about the individual object that has called the method. 
#Without self, every time we changed one object's attributes, we'd change the attribute for
#all the items of that type. 

# class User(object):
#   name = "Anna"
# anna = User()
# print "anna's name: ", anna.name
# User.name = "Bob"
# print "anna's name after change:", anna.name
# bob = User()
# print "bob's name:", bob.name

#I still don't understand what i just did.
#Python's _init_ method is known as a magic method. Magic methods are automatically
#created and sometimes invoked when a new instance of a class is created. 
#_init_ is useful because it allows us to set some attributes when a new instance is created.
#Because we know that the init method will run immediately, we can pass in some parameters
#to that init method upon object creation.

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = False
user1 = User("Anna Propas", "anna@anna.com")
print user1.name
print user1.logged
print user1.email

#Above we are able to create objects that share characteristics but are still individual. When
#the object is created we can specify what values we'd like to assign to each attribute. 
#In the _init_ method we are assigning the values we passed in as values of the attributes
#of each individual object.
