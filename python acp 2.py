import random
turn_off = True
number = random.randint(1, 100)
while turn_off:
    print("guess number")
    x = int(input(""))
    if x == number:
        print("YOU WIN")
        turn_off = False
    elif x > number:
        print("too high")
    elif x < number:
        print("too low")