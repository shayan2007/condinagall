class math:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    def addition(self):
        print(self.num1+self.num2+self.num3)

obj1 = math(1, 2, 3)
obj1.addition()