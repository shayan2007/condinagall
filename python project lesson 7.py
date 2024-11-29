class A1:
    species = "almost human"
    def __init__(self, name, age, brain, insane):
        self.name = name
        self.age = age
        self.brain = brain
        self.insane = insane
    
    def changename(self, name):
        self.name = name
    
    def intro(self):
        print(f"hello i am {self.name} i am {self.age} years old")
        if self.brain:
            print("i have a brain")
        if self.insane:
            print("i am insane")

thing1 = A1("siebel", -200, False, True)
thing2 = A1("shayan", 17, True, True)

thing1.changename("Siebel")
thing2.changename("Shayan")
thing1.intro()
thing2.intro()