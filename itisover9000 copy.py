n = abs(int(float(input("enter a number: "))))

count = 0
if n == 0:
    print("you know the answer")
    exit("poo")
if (n & (n & ~(n-1))):
    while(n > 1):
        n >>= 1
        count += 1

if count % 2 == 0:
    print("yes its power is over 4")
else:
    print("no its power is not over 4")