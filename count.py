n = abs(int(float(input("ONLY NUMBER: "))))
zero = 0
one = 0
while (n):
    if (n&1==1):
        one += 1
    else:
        zero += 1
    n >>= 1

print("ones:", one)
print("zeros:", zero)