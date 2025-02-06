n = abs(int(float(input("enter a number: "))))

count = 1
flag = True
while (flag):
    temp = n >> 1
    temp2 = temp << 1
    if temp2 == n:
        count = count + 1
        n = temp
    else:
        flag = False

print("bit at:", count)