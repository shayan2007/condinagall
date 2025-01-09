def deaf(n):
    if(n == 0):
        print("cry about it")
        return 0
    else:
        print(n)
        return n + deaf(n-1)


print("995")
print(deaf(995))
