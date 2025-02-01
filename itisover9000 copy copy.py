x = abs(int(float(input("enter a number: "))))
y = abs(int(float(input("enter another number: "))))
r = 1
while(y>0):
    if y%2==0:
        x=x*x
        y>>=1
    else:
        r=r*x
        y-=1
print(r)