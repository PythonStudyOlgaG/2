"""
4. Программа .
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""
def my_func(x: float, y: int) -> float:
    """
    Функция принимает действительное положительное число x и целое отрицательное число y,
    выполняет возведение числа x в степень y двумя способами.
    """
    input_way = input("Введите способ реализации (1 или 2): 1) **; 2) цикл: \n")
    if input_way == str(1):
        result = abs(x) ** (y * (-1))
    elif input_way == str(2):
        count = 0
        result = 1
        for count in range(y):
            result = (1 / abs(x)) * result
            count += 1
    return print(result)

call = my_func(0.001, 0)