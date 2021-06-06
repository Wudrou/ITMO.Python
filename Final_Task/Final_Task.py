import csv
import time
import datetime

rows = []
title = ["CATEGORY", "PRODUCT", "COST", "DATE"]

def menu():
    print("Hello")

    def show_menu():
        print("\n1. Add")
        print("2. Show all")
        print("3. Show for date")
        print("4. Show by category")
        print("5. Show by min->max")
        print("6. Delete")
        print("0. Exit")

    err_msg = "\nВведена неверная команда. Необходимо ввести команду от 0 до 6"

    while True:
        show_menu()
        try:
            choice = int(input("Введите команду: "))
        except ValueError:
            print(err_msg)
            continue
        if choice == 1:
            print("\nДобавление записи.")
            add()
        elif choice == 2:
            print("\nПоказать все записи.")
            show_all()
        elif choice == 3:
            print("\nПоказать записи по дате.")
            show_param(3)
        elif choice == 4:
            print("\nПоказать записи по категории")
            show_param(0)
        elif choice == 5:
            print("\nПоказать записи по возрастанию цены.")
            sort()
            show_all()
        elif choice == 6:
            print("\nУдаление записей.")
            delete()
        elif choice == 0:
            print("\nВыход из программы...")
            break
        else:
            print(err_msg)

def read_file():
    global rows
    try:
        with open("data.csv") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            rows = list(reader)
    except IOError:
        print("Ошибка чтения файла или файл не существует")
        file = open("data.csv", "w+")
        print("Исправляем...")
        time.sleep(2)
        print("Готово!\n")
        menu()

def add():
    row = []
    category = input("Введите категорию: ")
    row.append(category)
    prod = input("Введите продукт: ")
    row.append(prod)
    while True:
        try:
            cost = int(input("Введите стоимость: "))
        except ValueError:
            print("Введите корректную стоимость.")
            continue
        else:
            break
    row.append(cost)
    while True:
        try:
            year = int(input("Введите год: "))
            mon = int(input("Введите месяц: "))
            day = int(input("Введите день: "))
            dt = datetime.date(year, mon, day)
        except ValueError:
            print("Введена недействительная дата. Необходимо дату в правильном формате")
            continue
        else:
            break
    row.append(dt)
    rows.append(row)
    with open('data.csv', "w", newline="") as csvfile:
        output = csv.writer(csvfile)
        for row in rows:
            output.writerow(row)

def show_all():
    print("\n{: <20} {: <20} {: <20} {: <20}".format(*title))
    for row in rows:
        print("{: <20} {: <20} {: <20} {: <20}".format(*row))

def show_param(column):
    param = set()
    for row in rows:
        param.add(row[column])
    tmp = list(param)
    for n, item in enumerate(tmp):
        print(n+1, item)
    err_msg = "Введен неправильный номер параметра. Необходимо ввести номер от 1 до " + str(len(param))
    while True:
        try:
            choice = int(input("Для возврата введите 0.\nВведите номер параметра: "))
        except ValueError:
            print(err_msg)
            continue
        if choice in range(1, len(tmp) + 1):
            print("\n{: <20} {: <20} {: <20} {: <20}".format(*title))
            for row in rows:
                if row[column] == tmp[choice-1]:
                    print("{: <20} {: <20} {: <20} {: <20}".format(*row))
            break
        elif choice == 0:
            break
        else:
            print(err_msg)

def sort():
    rows.sort(key=lambda row: int(row[2]))

def delete():
    file = open("data.csv", "w+")
    file.close()
    read_file()
    time.sleep(1)
    print("\nВсе записи удалены.")
          
read_file()
menu()
