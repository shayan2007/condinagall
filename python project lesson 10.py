class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def intro(self):
        print(f"i am a dog named {self.name}, i am {self.age} years old")
    
    def sound(self):
        print("meow")

class cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def intro(self):
        print(f"i am a cat named {self.name}, i am {self.age} years old")
    
    
    def sound(self):
        print("woof")

class potato:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def intro(self):
        print(f"i am a potato named {self.name}, i am {self.age} years old")
    
    
    def sound(self):
        print("...")

obj1 = dog("obj1", 0.0001)
obj2 = cat("obj2", 0.0001)
obj3 = potato("obj3", 300)
for i in [obj1, obj2, obj3]:
    i.intro()
    i.sound()