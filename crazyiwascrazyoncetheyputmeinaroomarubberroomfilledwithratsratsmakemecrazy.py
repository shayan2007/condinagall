a = 10
b = -10
print("a:", a)
print("b:", b)
a = a^b
b = a^b
a = a^b
print("a:", a)
print("b:", b)
a = (a&b) + (a|b)
b = a + ~b + 1
a = a + ~b + 1
print("a:", a)
print("b:", b)
#other way
print("a:", b)
print("b:", a)
