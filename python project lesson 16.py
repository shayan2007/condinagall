numbere = int(input("numbre: "))
didi = len(str(numbere))
res = 0
temp = numbere
while temp > 0:
    digit = temp % 10
    res += digit ** didi
    temp //= 10

if numbere == res:
    print(numbere)
else:
    print("cry about it")