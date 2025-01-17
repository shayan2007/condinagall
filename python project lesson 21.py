from math import sqrt
num = int(float(input("num: ")))
if num > 1:
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            print("not octopus prime")
            exit(-1)
else:
    print("not optimus prime")
    exit(-1)

print("guess it was octupus optimus prime")