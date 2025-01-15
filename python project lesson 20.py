larg = int(float(input("big: ")))
smol = int(float(input("smol: ")))
if larg < 0:
    exit("no")
if smol < 0:
    exit("no")
if larg < smol:
    temp = larg
    larg = smol
    smol = larg

while smol:
    temp = smol
    smol = larg % smol
    larg = temp

print(larg)