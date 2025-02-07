import math
set = "shayan"
setsiz = 6
powersetsiz = int(math.pow(2, setsiz))
outer = 0
inner = 0

for outer in range(0, powersetsiz):
    for inner in range(0, setsiz):
        if (outer & (1<<inner)) > 0:
            print(set[inner], end = "")
    print("")

