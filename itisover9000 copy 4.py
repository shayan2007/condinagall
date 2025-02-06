listofprim = []
import math

for i in range(10, 99):
    flag = True
    for e in range(2, int(math.sqrt(i))+1):
        if i % e == 0:
            flag = False
    if flag == True:
        listofprim.append(i)
print(listofprim)