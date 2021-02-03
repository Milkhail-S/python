from functools import reduce


def multi(current, nekst):
    return current * nekst


sotki = [sot for sot in range(100, 1001) if sot % 2 == 0]
print(reduce(multi, sotki))
