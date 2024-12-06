class library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lendDict = {}
        self.lendTime = {}
    

    def updatebok(self):
        for i in self.lendTime.keys():
            self.lendTime[i] = self.lendTime[i] -1

    def displayBooks(self):
        print(f"we have books this {self.name}")
        for bok in self.booklist:
            print(bok)

    def lendMONEY(self, user, bok):
        if bok in self.booklist:
            if(bok not in self.lendDict.keys()):
                self.lendDict.update({bok:user})
                self.lendTime.update({bok:5})
                print("give bok back before the 5th")
            else:
                print("no bok")
        else:
            print("no")
            exit(-420)

    def addbook(self, bok):
        if bok in self.booklist:
            print("extra no")
            exit(-420)
        self.booklist.append(bok)
        print("bok boked")
    
    def returnbok(self, user, bok):
        if(bok in self.lendDict.keys()):
            if self.lendTime[bok] <= 0:
                print("BOK BOK PAY EXTRA")
            self.lendDict.pop(bok)
        else:
            print("who you tring to scam")
x = input("name\n")
libr = library([], x)
    
while True:
    x = input("what do you want to do(1 display, 2 add, 3 lend, 4 return)\n")
    if x == "1":
        libr.displayBooks()
    elif x == "2":
        name = input("name of new bok\n")
        libr.addbook(name)
    elif x == "3":
        user = input("who want bok\n")
        bok = input("which bok\n")
        libr.lendMONEY(user, bok)
    elif x == "4":
        bok = input("which bok return\n")
        user = input("who\n")
        libr.returnbok(user, bok)
    else:
        print("no")
    libr.updatebok()