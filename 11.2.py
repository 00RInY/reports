
"""
2. Из заданной строки отобразить только символы нижнего регистра. Использовать
библиотеку string. Строка'In PyCharm, you can specify third-party standalone applications and
run them as External Tools'.
"""
import string
s = 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'

r = ''
for mal in s:
    if mal in string.ascii_lowercase:
        r += mal

print(r)
