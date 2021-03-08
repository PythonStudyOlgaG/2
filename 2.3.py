"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
import time


# решение через list
def month_list():
    """
    Определяет время года по номеру месяца.
    Дополнительно реализован расчет времени выполнения программы.
    """
    list_start_time = time.time()
    list_input_int = input_int
    season = ""
    if list_input_int in [12, 1, 2]:
        season = "winter"
    elif list_input_int in [3, 4, 5]:
        season = "spring"
    elif list_input_int in [6, 7, 8]:
        season = "summer"
    elif list_input_int in [9, 10, 11]:
        season = "autumn"
    else:
        season = "Введено число вне диапазона"
    time.sleep(0.01)
    return print(season, f"{(time.time() - list_start_time):.3f}")


# решение через dict
def month_dict():
    """
    Определяет время года по номеру месяца.
    Дополнительно реализован расчет времени выполнения программы.
    """
    dict_start_time = time.time()
    dict_input_int = input_int
    season_dict = {"Winter": (1, 2, 12),
                   "Spring": (3, 4, 5),
                   "Summer": (6, 7, 8),
                   "Autumn": (9, 10, 11)}
    for key in season_dict.keys():
        if dict_input_int in season_dict[key]:
            time.sleep(0.01)
            return print(key, f"{(time.time() - dict_start_time):.3f}")


input_int = int(input("Введите номер месяца от 1 до 12 для определения времени года:\n"))
input_str = input("Введите list или dict")
output = None
if input_str == "list":
    output = month_list()
elif input_str == "dict":
    output = month_dict()
else:
    output = "Введено число вне диапазона"
print(output)
