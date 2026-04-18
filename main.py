def hisobla(tomonlar, burchaklar):
    import math
    s = 0
    for i in range(len(tomonlar)):
        a, b, c = tomonlar[i]
        A, B, C = math.radians(burchaklar[i][0]), math.radians(burchaklar[i][1]), math.radians(burchaklar[i][2])
        s += 0.5 * a * b * math.sin(C)
    return s

tomonlar = [[3, 4, 5], [6, 8, 10]]
burchaklar = [[60, 60, 60], [30, 60, 90]]
print(hisobla(tomonlar, burchaklar))
