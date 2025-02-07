n = abs(int(float(input("number: "))))

hippo = [0, 1]
for i in range(n):
    hippo.append(hippo[-1]+hippo[-2])


for i in range(n):
    print(hippo[i])