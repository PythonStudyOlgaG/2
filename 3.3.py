"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(arg_1: float, arg_2: float, arg_3: float) -> float:
    """
    Функция my_func() принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов
    :param arg_1:
    :param arg_2:
    :param arg_3:
    """
    max_1 = max(arg_1, arg_2, arg_3)
    if max_1 == arg_1:
        max_2 = arg_2 if arg_2 >= arg_3 else arg_3
    elif max_1 == arg_2:
        max_2 = arg_1 if arg_1 >= arg_3 else arg_3
    elif max_1 == arg_3:
        max_2 = arg_1 if arg_1 >= arg_2 else arg_2
    return print(max_1 + max_2)


call = my_func(1, 11, 2)
