a = abs(int(float(input("ONLY NUMBER a: "))))
b = abs(int(float(input("ONLY NUMBER b: "))))
c = abs(int(float(input("ONLY NUMBER c: "))))



aandb = a&b
borc = b|c
candb = c&b
borcandcandb = borc&candb
aandborborcandcandb = aandb|borcandcandb
print("aandborborcandcandb:", aandborborcandcandb)