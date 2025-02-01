list_of_numero = [2, 2, 4, 6]
xorof2 = list_of_numero[0]
x = 0
y = 0

bit = 0
for i in range(1, len(list_of_numero)):
    xorof2 = xorof2 ^ list_of_numero[i]
bit = xorof2 & ~(xorof2-1)

for i in range(len(list_of_numero)):
    if list_of_numero[i] & bit:
        x = x ^ list_of_numero[i]
    else:
        y= y ^ list_of_numero[i]

print("x:", x)
print("y:", y)

