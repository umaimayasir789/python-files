#creating parent class
class person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
            print(self.fname,self.lname)
            #creating object 
x = person("john","doe")
            #calling
x.printname()
# task 5
# ineriting from parent class
class student(person):
    pass #inherit
x = student("mike","olsen")
x.printname()