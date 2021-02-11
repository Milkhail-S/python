class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name}: {self.speed} км/ч')

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'Машина {self.name} устремилась {self.direction}')

class TownCar(Car):
    def __init__(self,speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 60:
            print(f'Внимание! Ограничение скорости 60 км/ч')
            print(f'Превышение скорости на {self.speed -60} км/ч')
        else:
            print(f'Текущая скорость автомобиля {self.name}: {self.speed} км/ч')


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 40:
            print(f'Внимание! Ограничение скорости 40 км/ч')
            print(f'Превышение скорости на {self.speed - 40} км/ч')
        else:
            print(f'Текущая скорость автомобиля {self.name}: {self.speed} км/ч')

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

# Базовый класс:
c = Car(50, 'Brown', 'Ford')
print(f'Автомобиль марки {c.name}, цвета {c.color}, двигается со скоростью {c.speed}км/ч')
if c.is_police:
    print(f'Работает полиция! Всем прижаться к обочине!')
c.go()
c.stop()
c.turn('направо')
c.show_speed()
print('\n')
# Городской автомобиль:
t = TownCar(70, 'Blue', 'Renault')
print(f'Автомобиль марки {t.name}, цвета {t.color}, двигается со скоростью {t.speed}км/ч')
if t.is_police:
    print(f'Работает полиция! Всем прижаться к обочине!')
t.go()
t.stop()
t.turn('налево')
t.show_speed()
print('\n')
# Рабочий автомобиль:
w = WorkCar(53, 'Green', 'Jeep')
print(f'Автомобиль марки {w.name}, цвета {w.color}, двигается со скоростью {w.speed}км/ч')
if w.is_police:
    print(f'Работает полиция! Всем прижаться к обочине!')
w.go()
w.stop()
w.turn('в переулок')
w.show_speed()
print('\n')
# Полицейский автомобиль:
p = PoliceCar(70, 'Blue-White', 'Lada', True)
print(f'Автомобиль марки {p.name}, цвета {p.color}, двигается со скоростью {p.speed}км/ч')
if p.is_police:
    print(f'Работает полиция! Всем прижаться к обочине!')
p.go()
p.stop()
p.turn('в участок')
p.show_speed()
print('\n')
# Спортивный автомобиль:
s = SportCar(70, 'Red', 'Ferrari')
print(f'Автомобиль марки {s.name}, цвета {s.color}, двигается со скоростью {s.speed}км/ч')
if s.is_police:
    print(f'Работает полиция! Всем прижаться к обочине!')
s.go()
s.stop()
s.turn('в закат')
s.show_speed()
