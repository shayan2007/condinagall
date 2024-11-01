size = int(input("pee pee poo poo what is your nunmber to toilet too:\n"))
size = int(4*(size-0.5))
print(" ")
for y in range(size):
    for x in range(size):
        a = y
        b = x
        if a >= size/2:
            a = size-a-1
        if b >= size/2:
            b = size-b-1
        a = abs(a-size/2)
        b = abs(b-size/2)
        if a>b:
            c = a
        else:
            c = b
        L = size/2
        if size%4==0:
            L = L - 1
        if y == x+1 and y <= L:
                c = c + 1
        if (c+size/2)%2 == 0:
             print("x", end="")
        else:
             print(" ", end="")
    print("")
        