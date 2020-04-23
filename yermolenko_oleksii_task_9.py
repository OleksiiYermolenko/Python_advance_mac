# Домашнее задание 9
# Добавлено: 02.04.2020 20:01
# ДЗ 9
# Описать класс «домашняя библиотека». Предусмотреть возможность работы с произвольным числом книг,
# поиска книги по какому-либо признаку (например, по автору или по году издания),
# добавления книг в библиотеку, удаления книг из нее, сортировки книг по разным полям.



import csv
# while True:
#     answer = input("Would you like to add, list or exit? ")
#     if answer == "add":
#         name = input("What is your name? ")
#         phone_number = input("Input you number? ")
#         with open("yermolenko_oleksii_task_9.csv", "w") as file:
#             file.write("\n" + name + "," + phone_number)
#             continue
#
#     elif answer == "list":
#         with open('yermolenko_oleksii_task_9.csv', 'r') as file:
#             reader = csv.reader(file)
#             for row in reader:
#                 print(row)
#
#     elif answer == "exit":
#         print("Goodbye!")
#         break
#     else:
#         print("I'm sorry, that is not an option")

class MyHomeLibrary:
    # my_library = {}
    # with open("yermolenko_oleksii_task_9.csv", "r") as file:

    # def __init__(self, name, athor, year, libr_namb):
    #     self.name = name
    #     self.athor = athor
    #     self.year = year
    #     self.libr_numb = libr_namb

    # def input_info(self):
    #     pass


    # def add_book(self):
    #
    #     file.write("\n" + name + "," + phone_number)
    #     pass
    #
    def find_book(self):
        pass
    #
    def sort_book_number_up():
        with open("yermolenko_oleksii_task_9.csv", "r") as file:
            for row in csv.reader(file):
                print(row)

    def show_library():
        with open("yermolenko_oleksii_task_9.csv", "r") as file:
            for row in csv.reader(file):
                print(row)

    def remove_book(self):
        pass

MyHomeLibrary.show_library()