num = int(float(input("numbre: ")))
if num < 0:
    print("no")
    exit(-1)


for i in range(1, num+1):
    if(num%i==0):
        print(i)
