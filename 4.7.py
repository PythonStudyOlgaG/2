"""
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""

def factorial_g(item_n: int):
    if item_n == 0: yield 1
    factorial = 1
    for item in range(1, item_n + 1):
        factorial *= item
        yield factorial

input_item = int(input("Укажите факториал какого числа Вы хотели бы узнать?\n"))
for _ in factorial_g(input_item):
    print(_)


# далее разбиралась с рекурсией
def factorial_rec(item_n: int):
    if item_n == 0: return 1
    return item_n * factorial_rec(item_n - 1)


print("\nРекурсивно: \n", factorial_rec(input_item))
