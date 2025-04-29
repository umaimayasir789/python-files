class person:
    def __init__(mysillyobject,name,age):  #using a diff name instead of self
     mysillyobject.name = name
     mysillyobject.age = age
    def myfunc(abc):
       # using another name instead of self
       print("hello,my name is umaima")
       #creating an object
p1 = person("umaima",20)
       #calling func
p1.myfunc()
        