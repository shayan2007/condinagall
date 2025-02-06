n = abs(int(float(input("enter a number: "))))

count = 0

while (n):
    n = n >> 1
    if n > 0:
        count = count + 1

print("bit at:", count)