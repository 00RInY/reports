"""Дана строка '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15', отражающая средние
температуры по месяцам в году. Преобразовать информацию из строки в словарь, с
использованием функции найти среднюю и минимальные температуры, результаты
вывести на экран.
"""
data = "2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15"

parts = data.split()
year = parts[0]

temps = []
for i in parts[1:]:
    temps.append((int(i)))

temperature_dict = {year: temps}
print(temperature_dict)
min_temps = min(temps)
sred = sum(temps) / len(temps)
print(sred)
print(min_temps)
