class A1:
    species = "almost robot"
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

class A2:
    species = "tobor tsomla"
    def __init__(self, name, age, brain, insane):
        self.name = name
        self.age = age
        self.brain = brain
        self.insane = insane
    
    def changename(self, name):
        self.name = name
    
    def intro(self):
        print(f"dlo sraey {self.age} ma i {self.name} ma i olleh")
        if self.brain:
            print("niarb a evah i")
        if self.insane:
            print("enasni ma i")

x = input("english or giberish(1 or 2)")
if x == "1":
    robot = A1("bot", 1, True, False)
if x == "2":
    robot = A2("tob", 2, False, True)

robot.intro()