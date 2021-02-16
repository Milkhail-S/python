class Cell:
    def __init__(self, qty_cells: int):
        self.qty_cells = qty_cells

    @property
    def qty_cells(self):
        return self.__qty_cells

    @qty_cells.setter
    def qty_cells(self, qty_cells):
        if type(qty_cells) is int:
            self.__qty_cells = qty_cells
        else:
            print('Попробуйте ввести целое число клеток')

    def __add__(self, other):
        joint = self.qty_cells + other.qty_cells
        return Cell(joint)

    def __sub__(self, other):
        if self.qty_cells - other.qty_cells > 0:
            diff = self.qty_cells - other.qty_cells
        else:
            print('Клетка не может иметь отрицательные ячейки!')
            return
        return Cell(diff)

    def __mul__(self, other):
        multi = self.qty_cells * other.qty_cells
        return Cell(multi)

    def __truediv__(self, other):
        div = int(self.qty_cells / other.qty_cells)
        return Cell(div)

    def make_order(self, row=3):
        cell_view = ['*' for _ in range(self.qty_cells)]
        new_cell = ''.join(cell_view)
        while len(new_cell) > 0:
            print(new_cell[:row])
            new_cell = new_cell[:len(new_cell) - row]
        return '' #убирает вывод None. Не придумал как по-другому.

    def __str__(self):
        return f'Клетка\n{self.qty_cells}'


c1 = Cell(7)
c2 = Cell(3)
c3 = c1 + c2
print(c3.make_order(2))


