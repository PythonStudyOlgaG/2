"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
"""
class Warehouse():
    def __init__(self):
        self._wdict = {}

    def add_to(self, equipment):
        self._wdict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, reg_n):
         if self._wdict[reg_n]:
            self._wdict.setdefault(reg_n).pop(0)


class OfficeEquipment(Warehouse):
    def __init__(self, reg_n, w_place):
        self.reg_n = reg_n
        self.w_place = w_place
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.reg_n} {self.w_place}'


class Printer(OfficeEquipment):
    def __init__(self, series, reg_n, w_place):
        super().__init__(reg_n, w_place)
        self.series = series

    def __repr__(self):
        return f'{self.reg_n} {self.series} {self.w_place}'

    def action(self):
        return 'Печатает'


class Scaner(OfficeEquipment):
    def __init__(self, reg_n, w_place):
        super().__init__(reg_n, w_place)

    def action(self):
        return 'Сканирует'


class Xerox(OfficeEquipment):
    def __init__(self, reg_n, w_place):
        super().__init__(reg_n, w_place)

    def action(self):
        return 'Копирует'


sklad = Warehouse()
# создаем объект и добавляем
scaner = Scaner('S/hp/321', 90)
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
