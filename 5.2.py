"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
def read_file():
    num_lines = 0 #количество строк
    num_words = 0 #количество слов в строке
    arr = []
    with open("5.2.txt", "r") as mf:
        for line in mf:
            words = line.split()
            num_lines += 1
            num_words = len(words)
            arr.append(f"Строка: {num_lines}, в ней слов: {num_words}")
    return print(arr)

go = read_file()
