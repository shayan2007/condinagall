n = abs(int(float(input("enter a number: "))))

flag = False

while (n):
    temp = n >> 3
    temp2 = temp << 3
    if n == 1:
        print("yes")
        exit(0)
    if temp2 == n:
        n = temp
    else:
        print("no")
        exit(0)
