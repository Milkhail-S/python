class Warehouse:
    total = {}
    dep = {}

    def __str__(self):
        return f'{Warehouse.total}'

    @staticmethod
    def write_in(item):
        b = item.__class__.__name__
        if Warehouse.total.get(b) is None:
            Warehouse.total.setdefault(b, str(item))
        else:
            mid = [Warehouse.total.get(b)] # почему второе обращение затирает значение ключа?
            Warehouse.total[b] = mid.append(str(item))

    def write_off(self, item, dep):
        pass


class Orgtechnika:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.orgtech_piece = {
            'brand': brand,
            'model': model,
        }


class Printer(Orgtechnika):
    def __init__(self, brand, model, color_print=False):
        super().__init__(brand, model)
        self.printer_pcs = {
            'brand': brand,
            'model': model,
            'color_print': color_print,
        }

    def __str__(self):
        return f'{self.printer_pcs}'


class Scanner(Orgtechnika):
    paper_size = ['A4', 'A3', 'A2', 'A1']

    def __init__(self, brand, model, i=0):
        self.i = i
        super().__init__(brand, model)
        self.scanner_pcs = {
            'brand': brand,
            'model': model,
            'paper_size': Scanner.paper_size[self.i]
        }

    def __str__(self):
        return f'{self.scanner_pcs}'

    @property
    def i(self):
        return self.__i

    @i.setter
    def i(self, i):
        if 0 <= i <= 3:
            self.__i = i
        else:
            print('Неверный тип бумаги')
            for ind, el in enumerate(Scanner.paper_size, 1):
                print(ind, el)
            self.__i = int(input('Выберите тип бумаги: '))
            self.__i -= 1


class Xerox(Orgtechnika):
    copy_speed = ['10pgs/min', '30pgs/min', '70pgs/min', '100pgs/min']

    def __init__(self, brand, model, i=0):
        self.i = i
        super().__init__(brand, model)
        self.xerox_pcs = {
            'brand': brand,
            'model': model,
            'copy_speed': Xerox.copy_speed[self.i]
        }

    def __str__(self):
        return f'{self.xerox_pcs}'

    @property
    def i(self):
        return self.__i

    @i.setter
    def i(self, i):
        if 0 <= i <= 3:
            self.__i = i
        else:
            print('Неверный вариант')
            for ind, el in enumerate(Xerox.copy_speed, 1):
                print(ind, el)
            self.__i = int(input('Выберите скорость копирования: '))
            self.__i -= 1


s1 = Scanner('LG', 'lg550', 2)
s2 = Scanner('Samsung', 's6678', 0)
whs = Warehouse()
whs.write_in(s1)
print(whs.total['Scanner'])
whs.write_in(s2)
print(whs.total.get('Scanner'))
print(whs)
