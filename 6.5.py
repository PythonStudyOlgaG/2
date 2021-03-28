"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return print("\nЗапуск отрисовки")

class Pen(Stationery):
    def draw(self):
        return print(f"\nЗапуск отрисовки {Pen.__name__}, {self.title}")
    def width(self):
        return print(f"\nШирина штриха 0,5")

class Pencil(Stationery):
    def draw(self):
        return print(f"\nЗапуск отрисовки {Pencil.__name__}, {self.title}")
    def width(self):
        return print(f"\nШирина штриха 0,7")

class Handle(Stationery):
    def draw(self):
        return print(f"\nЗапуск отрисовки {Handle.__name__}, {self.title}")
    def width(self):
        return print(f"\nШирина штриха 1,2")

pen = Pen('ручкой')
print(pen.draw(), pen.width())
pencil = Pencil('карандашем')
print(pencil.draw(), pencil.width())
handle = Handle('маркером')
print(handle.draw(), handle.width())