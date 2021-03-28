"""
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных
на уроках по ООП.
"""
class Warehouse():
    def __init__(self): #Полиморфизм.
        self._wdict = {}

    def add_to(self, equipment):
        self._wdict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, reg_n):
         if self._wdict[reg_n]:
            self._wdict.setdefault(reg_n).pop(0)


class OfficeEquipment(Warehouse):
    def __init__(self, reg_n, w_place):#Полиморфизм.
        self.reg_n = reg_n
        self.w_place = w_place
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.reg_n} {self.w_place}'


class Printer(OfficeEquipment):
    def __init__(self, series, reg_n, w_place):#Полиморфизм.
        super().__init__(reg_n, w_place) #Наследование. Вызов метода инициализации родителя(OfficeEquipment)
        self.series = series

    def __repr__(self):
        return f'{self.reg_n} {self.series} {self.w_place}'

    def is_alive(self):
        return 'Печатает'


class Scaner(OfficeEquipment):
    def __init__(self, reg_n, w_place):
        super().__init__(reg_n, w_place)

    def _is_alive(self): #Инкапсуляция. Приватный метод.
        return 'Сканирует'


class Xerox(OfficeEquipment):
    def __init__(self, reg_n, w_place):
        super().__init__(reg_n, w_place)

    def is_alive(self):
        return 'Копирует'


sklad = Warehouse()
# создаем объект и добавляем
scaner = Scaner('S/hp/321', 90)
print(scaner._is_alive())
sklad.add_to(scaner)
scaner = Scaner('S/hp/311', 97)
sklad.add_to(scaner)
xerox = Xerox('S/hp/300', 99)
sklad.add_to(xerox)
printer = Printer('e-320', 'P/sony/115', 102)
sklad.add_to(printer)
# выводим склад
print(sklad._wdict)
# забираем с склада и выводим склад
sklad.extract('Scaner')
print()
print(sklad._wdict)