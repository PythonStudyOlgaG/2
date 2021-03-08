"""
2. (1) Для списка реализовать обмен значений соседних элементов, т.е.
   (2) Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
   (3) При нечетном количестве элементов последний сохранить на своем месте.
      Для заполнения списка элементов необходимо использовать функцию input().

"""
# Для заполнения списка элементов необходимо использовать функцию input().
input_list = list(input("Введите список\n"))

copy_list = input_list.copy()
last_element = copy_list.pop()
new_list = []
counter = 0
if len(input_list) % 2 == 0:
    for counter in range(0, len(input_list), 2):
#(2) Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
        new_list.append(input_list[counter+1])
        new_list.append(input_list[counter])
        counter += 2
#(3) При нечетном количестве элементов последний сохранить на своем месте.
else:
    for counter in range(0, len(input_list)-1, 2):
        new_list.append(input_list[counter+1])
        new_list.append(input_list[counter])
        counter += 2
    new_list.append(last_element)

print(new_list)