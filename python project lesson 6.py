THINGS = ((1, "Shayan", "monkey"), (2, "ma'am", "panda"), (3, "condingal", "pig"), (4, "siebel", "pig"))
dictionary = {}
speepees = set()
for i in THINGS:
    dictionary.update({i[0]:i[1:]})
    speepees.add(i[2])






print(THINGS)
print(dictionary)
print(speepees)