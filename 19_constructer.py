#constructer is basically a init function
#all the classes have function called __init__(), which is always excuted when the object is being initiated.
class student :
    def __init__(self, fullname):
        self.name = fullname
        print("adding new student to database")

s1 = student("ajim")
print(s1.name)

#the self parameter is a reference to the current object of the class and it is used to access variable that belong to class 