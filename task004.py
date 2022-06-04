# Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
# Найдите сумму всех простых чисел меньше двух миллионов.

def simple_multipliers(n):
    simple_mult = []
    for i in range(n + 1):
        simple_mult.append(i)
    simple_mult[1] = 0
    i = 2
    while i <= n:
        if simple_mult[i] != 0:
            j = i + i
            while j <= n:
                simple_mult[j] = 0
                j = j + i
        i += 1
    simple_mult = set(simple_mult)
    simple_mult.remove(0)
    return simple_mult

print(sum(simple_multipliers(2000000)))