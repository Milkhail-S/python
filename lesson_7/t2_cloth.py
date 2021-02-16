from abc import ABC, abstractmethod


class Cloth(ABC):
    @abstractmethod
    def cloth_calc(self):
        pass


class Coat(Cloth):
    def __init__(self, v: int):
        self.v = v

    def cloth_calc(self):
        qty_of_textile = self.v / 6.5 + 0.5
        return qty_of_textile


class Suit(Cloth):
    def __init__(self, h: float):
        self.h = h

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        if h > 2.2:
            self.__h = 2.2
        elif h < 0.5:
            self.__h = 0.5
        else:
            self.__h = h

    def cloth_calc(self):
        qty_of_textile = self.h * 2 + 0.3
        return qty_of_textile



"""Расчёт общего требуемого количества ткани.
При вызове с 1 аргументом требуем второй. При вызове с 2 аргументами говорит, что 3 это уже слишком:
TypeError: __init__() takes 2 positional arguments but 3 were given
Как вызвать super() правильно?
"""

class Fullset:

    def full_textile(self, v, h):
        a = Coat(v)
        b = Suit(h)
        f_set = a.cloth_calc() + b.cloth_calc()
        return f_set


palto = Coat(52)
kostyum = Suit(2.5)
p = palto.cloth_calc()
k = kostyum.cloth_calc()
print(p, k)
print(p + k)
f = Fullset()
print(f.full_textile(52, 2.5))
# print(f)
