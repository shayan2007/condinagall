
def pal(num):
    if num >= 10:
        if num <= 99:
            print(num)

def prime(num):
    prime = [True for i in range(num+1)]
    p = 2
    while p *p <=num:
        if prime[p] == True:
            for i in range(p*p, num+1, p):
                prime[i] = False
        p += 1
    for p in range(2, num+1):
        if prime[p]:
            pal(p)

num = int(float(input("num: ")))
prime(num)