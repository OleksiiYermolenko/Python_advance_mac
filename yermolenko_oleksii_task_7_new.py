import requests
import time


# Домашнее задание 7
# Добавлено: 26.03.2020 20:11
# ДЗ 7
# +1 Написать декоратор который будет выводить на экран время выполнения функции.

def func_time_counter(func):
    def wrapper():
        start_time = time.time()
        func()
        finish_time = time.time()
        print(f'Time: {finish_time - start_time} sec.')

    return wrapper


@func_time_counter
def time_req_webpage():
    webpage = requests.get('https://ithillel.ua/')

# time_req_webpage()


# +2 Сформировать убывающий массив из чисел, которые делятся на 3. Длину вводит пользователь
# def decr_array(quantity):
#     array = []
#     for i in range(3, quantity * 3 + 1):
#         if i % 3 == 0:
#             array.append(i)
#     array.reverse()
#     print(array)
#     return decr_array
#
#
# try:
#     quantity_of = int(input('Input quantity of decreasing array: '))
#     decr_array(quantity_of)
# except ValueError:
#     print('Please input integer!!!')


# +3 Написать декоратор skip который не выполняет функцию.
# Декоратор может принимать параметр который выдаст функция вместо реального результата

# ??? Есть-ли какой-то метод для функции с помощью которого можно
# сделать проверку на наличие аргументов у функции
#
# def skip(func):
#     def wrapper(*arg, **kwargs):
#         print(*arg, **kwargs)
#     return wrapper
#
#
# @skip
# def print_full_name(first_name, last_name):
#     print(f"My name is", first_name, last_name)
#
#
# # @skip
# def time_req_webpage():
#     webpage = requests.get('https://ithillel.ua/')

#
# print_full_name("Santa", "Clause")
# time_req_webpage()


# +4 Напишите генератор генерирующий последовательность треугольных чисел.

# def all_triangle_numbers(quantity):
#     number = 0
#     while number < quantity:
#         triangle_numbers = number * (number + 1) // 2
#         yield triangle_numbers
#         number += 1
#
# for n in all_triangle_numbers(20):
#     print(n)