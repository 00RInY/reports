import sqlite3

def add_d(cursor):
    name = input("Введите название дисциплины: ")
    spec = input("введите специальность: ")
    lec = int(input("введите кол лекционных часов: "))
    prac = int(input("введите кол прак часов: "))
    lab = int(input("введите кол лаб часов: "))
    otchet = input("Форма отчета: ")
    cursor.execute("INSERT INTO disciplini VALUES (?, ?, ?, ?, ?, ?, ?)", (
        None,
        name, 
        spec, 
        lec, 
        prac, 
        lab, 
        otchet))

def serch(cursor):
    print("1. Поиск по коду дисциплины")
    print("2. Поиск по специальности")
    print("3. Поиск по кол часов")

    choice = int(input())

    match choice:
        case 1:
            kod = int(input())
            cursor.execute("SELECT * FROM disciplini WHERE kod = ?",
                           (kod,))
            
            bd = cursor.fetchone()
            text(bd)
        case 2:
            spec = input("Введите спец: ")
            cursor.execute("SELECT * FROM disciplini WHERE specialnost LIKE ?",
                           ("%{spec}%",))
            bd = cursor.fethall()
            text(bd)
        case 3:
            m = int(input("Введите минимальное кол часов: "))
            cursor.execute("SELECT * FROM disciplini WHERE lecii+prakticheskie+lab >= ?",
                           (m,))
            bd = cursor.fetchall()
            text(bd)


def text(text):
    for bd in text:
        print(f"Название: {bd[0]}")
        print(f"Специальность: {bd[1]}")
        print(f"Лекции (часы): {bd[2]}")
        print(f"Практические (часы): {bd[3]}")
        print(f"Лабораторные (часы): {bd[4]}")
        print(f"Отчет: {bd[5]}")
        print("-"*25)

def delete(cursor):
    print("1. Удаление по коду дисциплины")
    print("2. Удаление по названию")
    print("3. Удаление по кол часов")

    choice = int(input())

    match choice:
        case 1:
            kod = int(input())
            cursor.execute("SELECT * FROM disciplini WHERE kod = ?",
                           (kod,))
            print(f"Было удалено {cursor.rowcount} строк")
        case 2:
            n = input("Введите название: ")
            cursor.execute("SELECT * FROM disciplini WHERE name LIKE ?",
                           ("%{n}%",))       
            print(f"Было удалено {cursor.rowcount} строк")
        case 3:
            kol = int(input("Введите макс кол часов: "))
            cursor.execute("SELECT * FROM disciplini WHERE lecii+prakticheskie+lab <= ?",
                           (kol,))
            print(f"Было удалено {cursor.rowcount} строк")

def update(cursor):
    print("1. Изменить название по коду ")
    print("2. Изменить часы по коду")
    print("3. Изменить спец п коду")

    choice = int(input())

    match choice:
        case 1:
            kod = int(input("Введите код: "))
            name = input("Введите новое название дисциплины: ")
            cursor.execute("UPDATE disciplini SET name = ? WHERE kod = ?",
                           (name, kod))
            print(f"Было обновлено {cursor.rowcount} записей")
        case 2:
            kod = int(input("Введите код: "))
            ch1 = int(input("Введите новое кол часов для лекций: "))
            ch2 = int(input("Введите новое кол часов для практических: "))
            ch3 = int(input("Введите новое кол часов для лаб: "))
            cursor.execute("UPDATE disciplini SET lecii = ?, prakticheskie = ?, lab = ? WHERE kod = ?",
                           (ch1, ch2, ch3, kod))
            print(f"Было обновлено {cursor.rowcount} записей")
        case 3:
            kod = int(input("Введите код: "))
            name = input("Введите новое название специальности: ")
            cursor.execute("UPDATE disciplini SET specialnost = ? WHERE kod = ?",
                           (name, kod))
            print(f"Было обновлено {cursor.rowcount} записей")


con = sqlite3.connect("plan3.db")

cursor = con.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS disciplini
                (kod INTEGER PRIMARY KEY AUTOINCREMENT, 
                name TEXT,
                specialnost TEXT,
                lecii INTEGER,
                prakticheskie INTEGER,
                lab INTEGER,
                otchet TEXT)
            """)


choice = -1
while choice != 0:
    print('1. Добавить запись')
    print('2. Поиск')
    print('3. Удаление')
    print('4. Редактирование')
    print('0. Выход')

    choice = int(input())

    match choice:
        case 1:
            add_d(cursor)
            con.commit()
        case 2:
            serch(cursor)
        case 3:
            delete(cursor)
            con.commit()
        case 4:
            update(cursor)
            con.commit()

con.commit()
con.close()