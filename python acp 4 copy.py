def func(n):
    print("1")
    print(n)
    if(n<0):
        print("1.1")
        return
    print("2")
    for i in range(0, n+1):
        print("2.1")
        print("codingal")
    print("3")
    func(int(n/2))
    func(int(n/3))


func(10)