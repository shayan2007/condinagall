a = int(float(input("what to divide:")))
b = int(float(input("by what: ")))
if (a < 0) ^ (b < 0):
    sgin = -1
else:
    sgin = 1

a = abs(a)
b = abs(b)
qn = 0
temp = 0
for i in range(31, -1, -1):
    if temp + (b<<i) <= a:
        temp += b << i
        qn |= 1<<i

qn = qn * sgin
print(qn)