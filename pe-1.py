def multiplesBelow(n, m):
    x = 0
    for y in range(1, n):
        if y % m == 0:
            x = x+y
    return x


print((multiplesBelow(1000, 3) + multiplesBelow(1000, 5))-multiplesBelow(1000, 15))
