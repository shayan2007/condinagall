romaning = {"M": 1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I": 1}
res = 0
put = input("number: ")
for i in range(0, len(put)-1):
    if romaning[put[i]] < romaning[put[i+1]]:
        res -= romaning[put[i]]
    else:
        res += romaning[put[i]]
res += romaning[put[-1]]
print(res)