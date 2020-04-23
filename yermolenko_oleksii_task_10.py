# Домашнее задание 10
# Добавлено: 06.04.2020 20:05
# ДЗ 10
# Разработка приложения для предметной области «Учёт товаров в магазине»
#
# Разработать приложение, позволяющее собирать и накапливать сведения о поступлении и реализации товаров некоторого магазина.
# Предусмотреть методы для вывода на экран отчетов, за день, за неделю, за месяц и за год.
# Отчеты короткие - приход, расход, прибыль.
#
#
#
# Учтите что программа рассчитана на долгое использование, то есть, после перезапуска программы данные не должны быть утеряны.
import datetime

class Warehouse:
    def __init__(self):
        pass


    def product(self):
        pass


    def add_product(self, data = datetime.datetime.now(), name, quantity):
        self.name = input("Name? ")
        phone_number = input("Input you number? ")
        with open("oleksii_yermolenko_oleksii_task_10.csv", "a") as file:
            file.write("\n" + data + "," + phone_number)
        

    def input_product(self):

        pass

    def sell_product(self):
        pass

import csv
while True:
    answer = input("Would you like to add, list or exit? ")
    if answer == "add":
        name = input("What is your name? ")
        phone_number = input("Input you number? ")
        with open("oleksii_yermolenko_task_21.csv", "a") as file:
            file.write("\n" + name + "," + phone_number)
            continue

    elif answer == "list":
        with open('oleksii_yermolenko_task_21.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    elif answer == "exit":
        print("Goodbye!")
        break
    else:
        print("I'm sorry, that is not an option")
