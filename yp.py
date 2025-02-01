n = abs(int(float(input("number: "))))
r = 0

while(n > 0):
    r = (r<<1) + (n&1)
    n >>= 1
print(r)