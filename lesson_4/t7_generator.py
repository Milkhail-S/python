def fact(n):
    i = 1
    a = 1
    while i <= n:
        yield a
        i += 1
        a *= i

for el in fact(4):
    print(el)
