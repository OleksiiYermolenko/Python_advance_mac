# Домашнее задание 3
# Добавлено: 06.03.2020 08:41
# Домашнее задание 4
# Правило идеального пользователя больше нет! Если я смог сломать Вашу программу - задача решена не верно.


# +1 Пользователь вводит число, если оно четное вывесть - “Even” если нет - “Odd”
# user_int = input('Please input integer: ')
# if user_int.strip("-").isdigit() or user_int.isdigit():
#     if int(user_int) % 2 == 0:
#         print('Odd')
#     else:
#         print('Even')
# else:
#     print("You'll try one more, please?")


# +2 Пользователь вводит значения через запятую, если количество значений меньше 10,
# отсортировать их от большего к меньшему, если больше то от меньшего к большему.

# user_string = input('Please input your string: ')
# user_string_test = user_string.replace(',', '')
# my_list = list(user_string.split(','))
# my_list = list(filter(None, my_list))
# len_string = len(my_list)
# if user_string_test.isdigit():
#     if len_string < 10:
#         sorted_list = sorted([int(item) for item in my_list])
#     else:
#         sorted_list = sorted([int(item) for item in my_list], reverse=True)
#
#     print(', '.join([str(elem) for elem in sorted_list]))
#
# else:
#     print("You'll try one more, please?")


# +3 Пользователь вводит 2 числа, если первое больше второго, вывести их разность, если второе больше первого вывести их
# сумму, если числа равны, возвести первое в степень второго.
# user_int_1 = input('Please input first integer : ')
# user_int_2 = input('Please input second integer: ')
# if (user_int_1.isdigit() or user_int_1.strip("-").isdigit()) and (
#         user_int_2.isdigit() or user_int_2.strip("-").isdigit()):
#     if int(user_int_1) > int(user_int_2):
#         print(int(user_int_1) - int(user_int_2))
#     elif int(user_int_1) < int(user_int_2):
#         print(int(user_int_1) + int(user_int_2))
#     else:
#         print(int(user_int_1) ** int(user_int_2))
# else:
#     print("You'll try one more, please?")


# +4 Пользователь вводит 3 числа, подставить и посчитать формулу: 2a - 8b / (a-b+c). Вывести результат.
# user_int_1 = input('Please input integer a: ')
# user_int_2 = input('Please input integer b: ')
# user_int_3 = input('Please input integer c: ')
#
# if (user_int_1.isnumeric() or user_int_1.strip("-").isnumeric()) and (
#         user_int_2.isnumeric() or user_int_2.strip("-").isnumeric()) and (
#         user_int_3.isnumeric() or user_int_3.strip("-").isnumeric()):
#     a = int(user_int_1)
#     b = int(user_int_2)
#     c = int(user_int_3)
#
#     print(2 * a - 8 * b / (a - b + c))
# else:
#     print("You'll try one more, please?")


# + 5 Дан список из целых чисел длиной N подсчитать количество четных чисел в списке
# my_list = [3, 5, 2, 4, 6, -7, 56, 34, 75, 33, 11, 8, 7]
# count = 0
# for item in my_list:
#     if item % 2 == 0:
#         count += 1
# print(count)



# 6 Дан список целых чисел длиной N отсортировать список, не используя метода sort или sorted. (Пожалуйста не гуглите
# решение, постарайтесь сделать сами)
# my_list = [2, 3, 5, 2, 4, 6, 7, 56, 34, 75, 33, 11, 8, 7]
# len_list = len(my_list)
# max_list = max(my_list)
# my_list_sort = []
# while len(my_list_sort) != len_list:
#     for item in my_list:
#         min_1 = min(my_list)
#         my_list_sort.append(min_1)
#         my_list.remove(min_1)
# print(my_list_sort)

# +7 Рассчитать последовательность фибоначчи, длину ряда задает пользователь
# longer_row = input('Please input long of Fibonacci row: ')
# fib_1 = fib_2 = 1
# if longer_row.isdigit():
#     if int(longer_row) > 1:
#         print(fib_1)
#         print(fib_2)
#         for i in range(2, int(longer_row)):
#             fib_1, fib_2 = fib_2, fib_1 + fib_2
#             print(fib_2)
#     else:
#         print("Why, so short row?")
# else:
#     print("You'll try one more, please?")




# +8 Пользователь вводит целое число, определить простое ли оно.
# user_int = input('Please input integer: ')
# int_two = 2
# if user_int.isdigit():
#     while int(user_int) % int_two != 0:
#         int_two += 1
#     if int_two == user_int:
#         print("Your number is prime")
#     else:
#         print("Your number is NO prime")
# else:
#     print("You'll try one more, please?")