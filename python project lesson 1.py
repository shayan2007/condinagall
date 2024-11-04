size = int(input("pee pee poo poo what is your nunmber to toilet too:\n"))
aplhabits = ["a", "b", "c", "d", "e", "f"]
print(" ")
for i in range(size):
    print(((size-i)*" ")+((3+(2*i))*aplhabits[i]))
for i in range(size):
    print((i*aplhabits[i]))
for i in range(size):
    print(((size-i)*" ")+((3+(2*i))*aplhabits[i]))
        