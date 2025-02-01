n = abs(int(float(input("enter a number: "))))


if n == 0:
    print("you know the answer")
    exit("poo")
if n & ~(n-1) == n:
    print("yes its power is over 2")
else:
    print("no its power is not over 2")