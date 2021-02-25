class DigitalOnly(Exception):
    def __init__(self, data, message='не число'):
        self.data = data
        self.message = message
        pass

    def __str__(self):
        return f'"{self.data}" - {self.message}'


spi = []
while True:
    try:
        a = input('Введите число или "stop": ')
        if a.isdigit():
            spi.append(int(a))
        elif a == 'stop':
            break
        else:
            raise DigitalOnly(a)
    except DigitalOnly as er:
        print(er)
        pass
print(spi)
