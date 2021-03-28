"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""
class ComplexNumber:
    def __init__(self, compl_1, compl_2):
        self.compl_1 = compl_1
        self.compl_2 = compl_2

    def __add__(self, other):
        result = f'{self.compl_1 + other.compl_1} + {self.compl_2 + other.compl_2} * i' if (self.compl_2 + other.compl_2) > 0 else f'{self.compl_1 + other.compl_1} {self.compl_2 + other.compl_2} * i'
        return print(result)


    def __mul__(self, other):
        result = f'{self.compl_1 * other.compl_1 - self.compl_2 * other.compl_2} + {self.compl_1 * other.compl_2 + (other.compl_1 * self.compl_2)} * i' if (self.compl_1 * other.compl_2 + (other.compl_1 * self.compl_2)) > 0 else f'{self.compl_1 * other.compl_1 - self.compl_2 * other.compl_2} {self.compl_1 * other.compl_2 + (other.compl_1 * self.compl_2)} * i'
        return print(result)


c_1 = ComplexNumber(3, 1)
c_2 = ComplexNumber(2, -3)
print(c_1 + c_2)
print(c_1 * c_2)