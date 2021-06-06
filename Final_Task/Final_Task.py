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

    err_msg = "\nВведена недействительная команда. Необходимо ввести команду от 0 до 6"

    while True:
        show_menu()
        try:
            choice = int(input("Введите команду: "))
        except ValueError:
            print(err_msg)
            continue
        if choice == 1:
            print("\nAdd:")
            add()
        elif choice == 2:
            print("\nShow all:")
            show_all()
        elif choice == 3:
            print("\nShow for date:")
            show_param(3)
        elif choice == 4:
            print("\nShow by category")
            show_param(0)
        elif choice == 5:
            print("\nShow by min -> max COST:")
            sort_cost()
            show_all()
        elif choice == 6:
            print("\nDelete:")
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
            print(err_msg)
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
    read_file()
    print("\n{: <20} {: <20} {: <20} {: <20}".format(*title))
    for row in rows:
        print("{: <20} {: <20} {: <20} {: <20}".format(*row))

read_file()
menu()
