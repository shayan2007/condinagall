num = int(float(input("poop: ")))
original = num
reversed = 0
while num > 0:
    digimon = num % 10
    reversed = reversed * 10 + digimon
    num //= 10
if original == reversed:
    print("it is your pal")
else:
    print("YOU YOU KNOW THE WEIGHT OF YOUR SINS YOU ABOSOLUTE FOOL CANT EVEN MAKE A NUMBER BE SYMETRICAL")