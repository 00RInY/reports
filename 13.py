"""
В исходном текстовом файле(Dostoevsky.txt) найти все варианты фамилии
Достоевского (т.е. с различными окончаниями, например, Достоевский,
Достоевского) в единственном экземпляре
"""

with open('Dostoevsky.txt', 'r', encoding='UTF-8') as file:
    text = file.read().split()

r = []

for ch in text:
    if ch.isalpha() and 'Дост' in ch:
        r.append(ch)
r = set(r)
print(r)
