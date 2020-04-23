# Домашнее задание 5
# Добавлено: 19.03.2020 20:00
# ДЗ 6
# Используйте функции по максимуму. Старайтесь всё что повторяется выносить в функции!
#
#
#
#
# +1. Написать программу перевода числа из арабских цифр в число из римских цифр.Написать программу обратного перевода.


# def int_to_roman(ara_num):
#     int_val = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
#                (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
#     rom_val = ''
#     ara_num = int(ara_num)
#     while ara_num > 0:
#         for i, j in int_val:
#             while ara_num >= i:
#                 rom_val += j
#                 ara_num -= i
#     return rom_val
#
#
# def roman_to_int(rom_num):
#     rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     int_val = 0
#     try:
#         for i in range(len(rom_num)):
#             if i > 0 and rom_val[rom_num[i]] > rom_val[rom_num[i - 1]]:
#                 int_val += rom_val[rom_num[i]] - 2 * rom_val[rom_num[i - 1]]
#             else:
#                 int_val += rom_val[rom_num[i]]
#         return int_val
#     except KeyError:
#         print(f'Strange symbols {rom_num} in your Roman number')
#
#
# print(roman_to_int('IXuXL'))
# print(roman_to_int('MMMM'))
# print(roman_to_int('C'))
# # #
# print(int_to_roman(500))
# print(int_to_roman(4000))
# print(int_to_roman(100))

# +2.  Написать функцию no_numbers которая удаляет из файла все цифры.
# Функция должна принимать путь к файлу.


# def no_numbers():
#     with open('text_doc_input.txt', 'r') as input_text:
#         symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#         txt_str = input_text.read()
#         for symbol in symbols:
#             if symbol in txt_str:
#                 txt_str = txt_str.replace(symbol, '')
#
#     with open('text_doc_output.txt', 'w') as output_text:
#         output_text.write(txt_str)


# C использованием регулярки получается покрасивше
# import re
#
#
# def no_numbers():
#     with open('text_doc_input.txt', 'r') as input_text:
#         txt_str = input_text.read()
#         txt_str = re.sub(r"[0123456789]", "", txt_str)
#
#     with open('text_doc_output.txt', 'w') as output_text:
#         output_text.write(txt_str)


# no_numbers()

#
#  +3. Написать функцию реализующую дешифровку Цезаря, функция должна принимать путь к файлу и сдвиг.
# def unkrypto_cezar(krypto_file, krypto_step):
#     with open(krypto_file, 'r') as input_file:
#         krypto_string = input_file.read()
#         list_of_numbers = '0123456789'
#         list_of_eng_abc_sm = 'abcdefghijklmnopqrstuvwxyz'
#         list_of_eng_abc_bi = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#         list_of_kir_abc_sm = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#         list_of_kir_abc_bi = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
#         text_len = len(krypto_string)
#         unkrypto_string = ""
#
#         if krypto_step.isdigit():
#             krypto_step = int(krypto_step)
#             for sim in range(0, text_len):
#                 kod_sth = ord(krypto_string[sim])
#
#                 if kod_sth in range(1, 47):
#                     unkrypto_string = unkrypto_string + chr(int(kod_sth))
#
#                 elif krypto_string[sim] in list_of_numbers:
#                     coded = list_of_numbers
#                     unkrypto_string = unkrypto_string + coded[(coded.index(krypto_string[sim]) - krypto_step) % len(coded)]
#
#                 elif krypto_string[sim] in list_of_eng_abc_sm:
#                     coded = list_of_eng_abc_sm
#                     unkrypto_string = unkrypto_string + coded[(coded.index(krypto_string[sim]) - krypto_step) % len(coded)]
#
#                 elif krypto_string[sim] in list_of_eng_abc_bi:
#                     coded = list_of_eng_abc_bi
#                     unkrypto_string = unkrypto_string + coded[(coded.index(krypto_string[sim]) - krypto_step) % len(coded)]
#
#                 elif krypto_string[sim] in list_of_kir_abc_sm:
#                     coded = list_of_kir_abc_sm
#                     unkrypto_string = unkrypto_string + coded[(coded.index(krypto_string[sim]) - krypto_step) % len(coded)]
#
#                 elif krypto_string[sim] in list_of_kir_abc_bi:
#                     coded = list_of_kir_abc_bi
#                     unkrypto_string = unkrypto_string + coded[(coded.index(krypto_string[sim]) - krypto_step) % len(coded)]
#                 else:
#                     unkrypto_string = unkrypto_string + krypto_string[sim]
#         else:
#             print('Sorry, your  krypto-step uncorrect.')
#         print(unkrypto_string)
#     with open('yermolenko_oleksii_task6_unkrypto.txt', 'w') as output_file:
#         output_file.write(unkrypto_string)
#
#
# unkrypto_cezar('yermolenko_oleksii_task6_krypto.txt', '2')
