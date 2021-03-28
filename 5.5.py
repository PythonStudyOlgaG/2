"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open("5.5.txt", "w+",) as sf:
    while True:
        input_s = input()
        if input_s == " ": break
        sf.write(input_s + "\n")

with open("5.5.txt", "r") as mf:
    items = mf.read().split()
    sum = 0
    for i in map(int, items):
        sum += i
    print(sum)