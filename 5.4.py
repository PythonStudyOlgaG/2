"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
try:
    with open('5.4.txt', 'r') as file_r:
        file_contents = []
        for line in file_r.readlines():
            file_contents.extend(line.rsplit())
    num = file_contents[2::3]
    rus = ["Один", "Два", "Три", "Четыре"]
except IOError:
    print("Произошла ошибка ввода-вывода!")
j = 0
try:
    with open('5.4_01.txt', 'w+') as file_w:
        for i in range(0, len(num)):
            file_w.write(str(rus[j] + " - " + num[i]) + "\n")
            j += 1
except IOError:
    print("Произошла ошибка ввода-вывода!")