"""
2. Из предложенного текстового файла (text18-9.txt) вывести на экран его содержимое,
количество букв в нижнем регистре. Сформировать новый файл, в который поместить текст
в стихотворной форме предварительно поставив последнюю строку фразой введенной
пользователем.
"""

def kol(n):
    l = 0
    for line in lines:
        for char in line:
            if char.islower():
                l += 1
    return l


with open('результат 2.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()

print("Содержимое файла:")
for line in lines:
    print(line.rstrip())

k = kol(lines)

print("Количество букв в нижнем регистре: ", k)

n = input("Введите фразу для последней строки: ")

lines.append(n)

with open('результат 2.txt', 'w', encoding='UTF-8') as new_file:
    new_file.writelines(lines)

print("Файл сохранен")

