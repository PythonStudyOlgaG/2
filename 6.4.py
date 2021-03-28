"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'\nМашина {self.name} поехала.'

    def stop(self):
        return f'\nМашина {self.name} остановилась.'

    def turn(self, direction):
        return f'\nМашина {self.name} повернула {direction}'

    def show_speed(self):
        return f'\nСпидометр показывает: {self.speed} км/ч'


class TownCar(Car):
    # переопределение метода show_speed
    def show_speed(self):
        if self.speed > 60:
            return f'\nВнимание! Превышение скоростного режима в 60 км/ч, скорость на спидометре: {self.speed}'
        else:
            return f'Машина {self.name} движется с приемлемой скоростью'


class SportCar(Car):
    pass


class WorkCar(Car):
    # переопределение метода show_speed
    def show_speed(self):
        if self.speed > 40:
            return f'\nВнимание! Превышение скоростного режима в 40 км/ч, скорость на спидометре: {self.speed}'
        else:
            return f'Машина {self.name} движется с приемлемой скоростью'


class PoliceCar(Car):
    pass


town_car = TownCar('Пежо', 70, 'синий', False)
print('1:\n' + town_car.go(), town_car.show_speed(), town_car.turn('направо'), town_car.turn('налево'), town_car.stop())

sport_car = SportCar('Лексус', 170, 'серый', False)
print('2:\n' + sport_car.go(), sport_car.show_speed(), sport_car.turn('направо'), sport_car.stop())

police_car = PoliceCar('Лада', 100, 'баклажан', True)
print('3:\n' + police_car.go(), police_car.show_speed(), police_car.turn('направо'), police_car.stop())

work_car = WorkCar('Белаз', 130, 'желтый', False)
print('4:\n' + work_car.go(), work_car.show_speed(), work_car.turn('направо'), work_car.stop())


