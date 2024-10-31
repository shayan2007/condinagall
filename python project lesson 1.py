x = int(input("pee pee poo poo what is your nunmber to toilet too:\n"))
alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(" ")
for i in range(x):
    print(((x-i)*" ")+((i+i+1)*alphabets[i])+(2*(x-i)*" ")+((i+i+1)*alphabets[i]))