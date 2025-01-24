n = abs(int(float(input("ONLY NUMBER: "))))
x = abs(int(float(input("ONLY bit: "))))
zero = 0
one = 0
for i in range(x-1):
    n >>= 1

if (n&1==1):
    print("SET")
else:
    print("CRY ABOUT IT")