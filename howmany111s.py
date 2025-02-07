n = 15

listofonelengths = [0]
count = 0
flag = False
while n>=0:
    if n&1:
        count += 1
        flag = True
    else:
        if flag:
            listofonelengths.append(count)
            count = 0
        flag = False
    if n == 0:
        n = -1
    n>>=1

print(max(listofonelengths))