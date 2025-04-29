class person:
    def __init__(self,name,age):  #constructor that initalize name and age
        self.name =  str(input("enter your name"))
        self.age =  int(input("enter the age"))

p2 = person ("umaima","20")

print(p2.name)
print(p2.age)

