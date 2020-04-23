# Дополнительные задачи:

# 1 Дана матрица 3х3. Вывести на экран первый и последний столбцы.
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# for row in matrix:
#     print(matrix[1[row]])

# 2 Пользователь вводит строку. Удалить из строки все символы, которые не являются буквами.
user_str = input('Please input your string: ')
print(user_str.count(user_str[-1]))

#+3 Пользователь вводит строку. Показать количество символов, совпадающих с последним символом строки.
# user_str = input('Please input your string: ')
# print(user_str.count(user_str[-1]))


# +4 Пользователь вводит количество недель, месяцев и лет. Вывести количество дней. Считать что в месяце 30 дней.
# user_week = input('Please input quantity of weeks: ')
# user_months = input('Please input quantity of months: ')
# user_years = input('Please input quantity of years: ')
#
# if user_week.isdigit() and user_months.isdigit() and user_years.isdigit():
#     if int(user_week) <= 56 and int(user_months) <= 12:
#         count = int(user_week) * 7 + 30 * (int(user_months) + int(user_years) * 12)
#         print(f"It's only {count} days")
#     else:
#         print('Strange quantity of months or weeks')
# else:
#     print("You'll try one more, please?")


# 5 Пользователь вводит число, вывести квадрат и куб числа.


# 6 Пользователь вводит цену за один кг печенья и за один кг конфет вывести стоимость:
# - одной покупки из 300г печенья и 400г конфет, трех покупок из 2кг печенья и 1кг 800г конфет


#7 Пользователь вводит пароль. Проверить этот пароль:
# - Пароль должен быть не короче 9 ти символов
# - Пароль должен содержать хотя бы одну цифру
# - В пароле должна быть хотя бы одна буква в верхнем регистре
