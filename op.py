import math
set = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
setsiz = 10
powersetsiz = int(math.pow(2, setsiz))
outer = 0
inner = 0

for outer in range(0, powersetsiz):
    for inner in range(0, setsiz):
        if (outer & (1<<inner)) > 0:
            print(set[inner], end = "")
    print("")

