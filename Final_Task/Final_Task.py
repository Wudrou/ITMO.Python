import csv
import time

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
            show_by(3)
        elif choice == 4:
            print("\nShow by category")
            show_by(0)
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
            inputcsv = csv.reader(csvfile, delimiter=',')
            rows = list(inputcsv)
    except IOError:
        print("Ошибка чтения файла или файл не существует")
        file = open("data.csv", "w+")
        print("Исправляем...")
        time.sleep(2)
        print("Готово!\n")
        menu()

def show_all():
    print("\n{: <20} {: <20} {: <20} {: <20}".format(*title))
    for row in rows:
        print("{: <20} {: <20} {: <20} {: <20}".format(*row))

read_file()
menu()
