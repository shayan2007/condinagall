def deaf(n):
    if(n == 0):
        print("cry about it")
    else:
        print(n)
        deaf(int(n/2))
        deaf(int(n/2))


print("10000000")
deaf(10000000)
