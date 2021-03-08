"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def quotient(divisible, divisor):
    """
    Функция quotient() выполняет деление чиел, вводимых пользователем.
    divisible - делимое
    divisor - делитель
    В случае деления на ноль выводится текстовое сообщение об ошибке
    """
    try:
        result = divisible / divisor
    except ZeroDivisionError:
        result = "Ошибка. Деление на 0"
    except ValueError:
        result = "Ошибка ввода ValueError"
    finally:
        return print(result)

arg_1 = float(input("Введите делимое:\n"))
arg_2 = float(input("Введите делитель:\n"))

quotient(arg_1, arg_2)

