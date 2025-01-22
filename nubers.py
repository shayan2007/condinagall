n = abs(int(float(input("ONLY NUMBER: "))))
count = 0
while n:
    count += 1
    n >>= 1
print(count)