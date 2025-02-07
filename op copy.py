import math
n1 = 10
n2 = 14


flop = 0
while (n1 > 0 or n2 > 0):
    t1 = (n1 & 1)
    t2 = (n2 & 1)
    if t1 != t2:
        flop += 1

    n1>>=1
    n2>>=1

print(flop)
print(n1)