def constant(n):
    print("consntantly rickrolling also", n) # very much something
    print("count 1")

def On(n):
    sum = 0
    count = 0
    for i in range(n+1):
        sum += i
        count += 1
    print("O(n) also", sum)
    print("count", count)

def On2(n):
    sum = 0
    count = 0
    for i in range(n+1):
        for j in range(i):
            sum += j
            count += 1
    print("O(n^2) also", sum)
    print("count", count)

constant(1)
On(1)
On2(1)
constant(100)
On(100)
On2(100)
constant(1000)
On(1000)
On2(1000)
