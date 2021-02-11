import time
from itertools import cycle


class Traffic_lights:
    def __init__(self, color):
        self.__color = color
    def running(self):
        t = {
            'Red': 7,
            'Yellow': 2,
            'Green': 5,
            }
        cl_chg = ['Red', 'Yellow', 'Green']
        pos = cl_chg.index(self.__color)
        count = 0
        switch_order = [0, 1, 2]
        if pos == 1:
            switch_order = [1, 2, 0]
        elif pos == 2:
            switch_order = [2, 0, 1]

        for i in cycle(switch_order):
            if count <6:
                print(cl_chg[i])
                time.sleep(t[cl_chg[i]])
                count += 1
            else:
                break

a = Traffic_lights('Yellow')
print(a._Traffic_lights__color)
a.running()
