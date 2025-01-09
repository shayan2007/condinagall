def deaf(n):
    if(n == 0):
        print("cry about it")
        return 0
    else:
        print(n)
        return n + deaf(n-1)


print("995")
print(deaf(995))

def blind(n):
    sum = 0
    for i in range(n):
        sum = sum + n
        print(n)
    return sum

print("10000000")
print(blind(10000000))