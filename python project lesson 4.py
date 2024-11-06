def truth(n):
    return truth_squared(n, 0)

def truth_squared(n, sum):
    if n == 0:
        return 0
    else:
        sum = sum + truth_squared(n-1, sum)
        return sum+n
    
def truth_second(n):
    if n == 0:
        return 0
    else:
        return truth_second_squared(n, 1)

def truth_second_squared(n, sum):
    if n == 0:
        return 1
    else:
        sum = truth_second_squared(n-1, sum)
        return sum*n
    

def overworking_elfs(gifts, elf_number):
    if gifts == 3:
        print(f"ELF NUMBER {elf_number} sent one present into the mouths of the greedy children and distributed the other 2 gifts to another poor sod of an elf")
        elf_number = elf_number + 1
        elf_number = overworking_elfs(2, elf_number)
        return elf_number
    elif gifts == 2:
        print(f"ELF NUMBER {elf_number} SENT 2 PRESENTS INTO THE MOUTHS OF THE GREEDY CHILDREN")
        elf_number = elf_number + 1
        return elf_number
    else:
        half_gifts = int(gifts/2)
        print(f"ELF NUMBER {elf_number} DISTRIBUTES, {half_gifts}")
        elf_numero_2 = overworking_elfs(half_gifts, elf_number+1)
        print(f"ELF NUMBER {elf_number} DISTRIBUTES {gifts-half_gifts}")
        elf_numero_2 = overworking_elfs(gifts-half_gifts, elf_numero_2)
        return elf_numero_2



print(truth(int(input("numeber \n"))))
print(truth_second(int(input("numeber \n"))))
overworking_elfs(int(input("numeber \n")), 1)



