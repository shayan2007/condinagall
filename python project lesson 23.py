
def pal(num):
    original = num
    reversed = 0
    while num > 0:
        digimon = num % 10
        reversed = reversed * 10 + digimon
        num //= 10
    if original == reversed:
        print(original)



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