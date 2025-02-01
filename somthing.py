n = abs(int(float(input("only number: "))))
counter = 1
while (n):
    if (n&1==1):
        print(counter)
        exit(0)
    else:
        counter += 1
    n >>= 1

print(0)
exit(0)