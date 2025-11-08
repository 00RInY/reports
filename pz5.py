#Составить программу, в которой функция генерирует четырехзначное число и
#определяет, есть ли в числе одинаковые цифры.
import random

def check(number):

    num_str = str(number)
    if len(set(num_str)) < len(num_str):
        return True  
    else:
        return False  
def d():

    return random.randint(1000, 9999)

gnumber = d()
print(f"Сгенерированное число: {gnumber}")

h = check(gnumber)

if h:
    print("В числе ЕСТЬ одинаковые цифры")
else:
    print("В числе НЕТ одинаковых цифр")
