# +1 Дан файл с текстом, создать список из дат в тексте - даты в формате DD-MM-YYYY (02-03-1999)
# from re import findall
#
#
# def date_list(file):
#     with open(file) as text:
#         text_start = text.read()
#         text_found = findall(r'\d{2}-\d{2}-\d{4}', text_start)
#         print(text_found)
#
#
# lst = date_list('yermolenko_oleksii_task_7.txt')

# +2 Пользователь вводит год в формате - YYYY (1999) Определить, является ли год високосным
# from re import match
#
#
# def what_year(year):
#     if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
#         print("Common year")
#     else:
#         print("Leap year")
#
#
# my_year = input('Please input year for checking:')
# if match(r"\d{4}", my_year):
#     what_year(int(my_year))
# else:
#     print('Uncorrected year, please input in format "YYYY"')

# +3 Дан файл вывести сумму всех чисел в файле.
# Цифры могут быть не целыми и отрицательными
# from re import findall, sub
#
#
# def number_sum(file):
#     numb_sum = 0
#     with open(file) as text:
#         text_start = text.read()
#         text_found = sub(r'\d{2}-\d{2}-\d{4}', " ", text_start)
#         text_found = findall(r"\d+\.\d+|-\d+\.\d+|\d+|-\d+", text_found)
#         for item, elem in enumerate(text_found):
#             text_found[item] = float(elem)
#             numb_sum = numb_sum + text_found[item]
#         print(text_found, numb_sum)
#
#
# number_sum('yermolenko_oleksii_task_7.txt')

# +4 Написать генератор геометрической прогрессии
# def geometric_progression(first_element, step, quantity):
#     counter = 1
#     while counter < quantity:
#         for quantity in range (1, quantity + 1):
#             n_element = first_element * step ** (quantity - 1)
#             yield n_element
#             counter += 1
#
# for elements in geometric_progression(-2, -2, 10):
#     print(elements)

#
#  +5 Дан файл с текстом, удалить из файла все отрицательные числа,
#  числа могут быть не целыми
# ??? как исключить шаблон \d{2}-\d{2}-\d{4} из замены чтобы исключить даты формата DD-MM-YYYY
# from re import sub
#
#
# def no_negative_number(file):
#     with open(file, 'r') as input_text:
#         txt_str = input_text.read()
#         txt_str = sub(r"^-\d+\.\d+|^-\d+|-\d+\.\d+|-\d+", "", txt_str)
#     with open('yermolenko_oleksii_task_7_no_neg.txt', 'w') as output_text:
#         output_text.write(txt_str)
#
#
# no_negative_number('yermolenko_oleksii_task_7.txt')


# 6 Дан файл с текстом, вывесли список который содержит все имена,
# все фамилии и все географические названия.
# Имена, Фамилии и Географические названии в простом формате, без дифисов.
#
#
# # В этом и всех последующих ДЗ можно использовать все библиотеки которые доступны в Python
#
# no_negative_number()
