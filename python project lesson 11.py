class obj1:
    def __init__(self, name, price, species):
        self.name = name
        self.__price = price
        self.species = species
    
    def intro(self):
        print(f"i am {self.name}, i am a {self.species}, i am for {self.__price} gold coins")

    def set_price(self, price):
        self.__price = price
    
obj2 = obj1("bob", 3, "human")
obj2.intro()
obj2.__price = 1
obj2.intro()
obj2.set_price(0)
obj2.intro()