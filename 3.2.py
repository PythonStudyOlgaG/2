"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def user_info(name, surname, birth_year, residence_city, email, phone_number) -> str:
    """
    Функция user_info принимает несколько параметров, описывающих данные пользователя:
    :param name:
    :param surname:
    :param birth_year:
    :param residence_city:
    :param email:
    :param phone_number:
    :return: вывод данных о пользователе реализован одной строкой (все параметры в одну строку)
    """
    user = "Имя: " + name + "| Фамилия: " + surname + "| Год рождения: " + birth_year + "| Город проживания: " + residence_city + "| Email: " + email + "| Номер телефона: " + phone_number
    return print(user)


i_name = input("Введите имя пользователя: \n")
i_surname = input("Введите фамилию пользователя: \n")
i_birth_year = input("Введите год рождения пользователя: \n")
i_residence_city = input("Введите город проживания пользователя: \n")
i_email = input("Введите email пользователя: \n")
i_phone_number = input("Введите телефон пользователя: \n")

user_info(i_name, i_surname, i_birth_year, i_residence_city, i_email, i_phone_number)
