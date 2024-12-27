def constant(n, m):
    print("consntantly rickrolling also", n*m) # very much something
    print("count 1")

def On(n, m):
    product = 0
    count = 0
    for i in range(n+1):
        product += m
        count += 1
    print("O(n) also", product)
    print("count", count)

def On2(n, m):
    product = 0
    count = 0
    for i in range(n+1):
        for j in range(i):
            product += m
            count += 1
    print("O(n^2) also", product)
    print("count", count)

constant(1, 1)
constant(100, 100)
On(1, 1)
On(100, 100)
On2(1, 1)
On2(100, 100)
