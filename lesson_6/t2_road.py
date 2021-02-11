class Road:
    def __init__(self, length, width):
        self._length = int(length)
        self._width = int(width)
    def massa(self, depth=1):
        self.m = 25
        mas = self._length * self._width * self.m * depth
        print(f'Для покрытия дорожного полотна\n шириной {self._width}м, длиной {self._length}м и толщиной {depth}см масса асфальта составит  = {mas}кг')

a = Road(5, 10)
a.massa(5)
