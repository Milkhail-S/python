class Stationery:
    title = 'Чертило'
    def draw(self):
        print(f'Программа "{self.title}": запуск отрисовки чем есть')

class Pen(Stationery):
    def draw(self):
        print(f'Программа "{self.title}": запуск отрисовки РУЧКОЙ')


class Pencil(Stationery):
    def draw(self):
        print(f'Программа "{self.title}": запуск отрисовки КАРАНДАШОМ')

class Handle(Stationery):
    def draw(self):
        print(f'Программа "{self.title}": запуск отрисовки МАРКЕРОМ')


s = Stationery()
s.draw()

p = Pen()
p.draw()

pnc = Pencil()
pnc.draw()

h = Handle()
h.draw()