# instantiate class User
class User(object):
  # this method to run every time a new object is instantiated
  def __init__(self, name, email):
    # instance attributes from
    self.name = name
    self.email = email
    self.logged = True
  
  def __repr__(self): #this allows you to print out an object instead of its memeory location when directly referencing the object
    return "<User object {}, email {}>".format(self.name,self.email)

if __name__ == "__main__":
  user = User("Anna", "anna@anna.com")
  print user