list_of_numero = []

n = abs(int(float(input("enter the number of elements: "))))
while(n):
    list_of_numero.append(abs(int(float(input(f"enter number {n}: ")))))
    n -= 1




thing = 0
for i in range(len(list_of_numero)):
    thing = list_of_numero[i]^thing
print(thing)

for i in range(len(list_of_numero)):
    occ = 0
    for e in range(len(list_of_numero)):
        if list_of_numero[i] == list_of_numero[e]:
            occ += 1
    if occ %2 == 1:
        print(list_of_numero[i])
