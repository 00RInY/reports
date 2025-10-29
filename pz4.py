#Дано целое число N (>0). Найти сумму 1 + 1/2 + 1/3 + ... + 1/N

N = input("Введите целое число N (>0): ")
while type(N) != int: # обработка исключений
    try:
        N = int(N)
    except ValueError:
        print("Неправильно ввели!")
        N = input("Введите число: ")

i = 1; s = 0
while i <= N:
    s += 1/i
    i += 1

print(s)
