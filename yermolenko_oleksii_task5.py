# ВАРИАНТ 3 конечный результат
with open('yermolenko_oleksii_task5_input.txt', 'r') as input_file:
    uncoded_string = input_file.read()
    key_step = input('please input step of krypto: ')
    list_of_numbers = '0123456789'
    list_of_eng_abc_sm = 'abcdefghijklmnopqrstuvwxyz'
    list_of_eng_abc_bi = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    list_of_kir_abc_sm = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    list_of_kir_abc_bi = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    text_len = len(uncoded_string)
    coded_string = ""

    if key_step.isdigit():
        key_step = int(key_step)
        for sim in range(0, text_len):
            kod_sth = ord(uncoded_string[sim])

            if kod_sth in range(1, 47):
                coded_string = coded_string + chr(int(kod_sth))

            elif uncoded_string[sim] in list_of_numbers:
                coded = list_of_numbers
                coded_string = coded_string + coded[(coded.index(uncoded_string[sim]) + key_step) % len(coded)]

            elif uncoded_string[sim] in list_of_eng_abc_sm:
                coded = list_of_eng_abc_sm
                coded_string = coded_string + coded[(coded.index(uncoded_string[sim]) + key_step) % len(coded)]

            elif uncoded_string[sim] in list_of_eng_abc_bi:
                coded = list_of_eng_abc_bi
                coded_string = coded_string + coded[(coded.index(uncoded_string[sim]) + key_step) % len(coded)]

            elif uncoded_string[sim] in list_of_kir_abc_sm:
                coded = list_of_kir_abc_sm
                coded_string = coded_string + coded[(coded.index(uncoded_string[sim]) + key_step) % len(coded)]

            elif uncoded_string[sim] in list_of_kir_abc_bi:
                coded = list_of_kir_abc_bi
                coded_string = coded_string + coded[(coded.index(uncoded_string[sim]) + key_step) % len(coded)]
            else:
                coded_string = coded_string + uncoded_string[sim]
    else:
        print('Sorry, your  krypto-step uncorrect.')

with open('yermolenko_oleksii_task5_output.txt', 'w') as output_file:
    output_file.write(coded_string)


#  Сначала сделал, как истинный лентяй ВАРИАНТ 1
# with open('yermolenko_oleksii_task5_input.txt', 'r') as input_file:
#     uncoded_string = input_file.read()
#     key_step = int(input('please input step of krypto: '))
#     print(uncoded_string)
#     text_len = len(uncoded_string)
#     coded_string = ""
#     for sim in range(0, text_len):
#         coded_string = coded_string + chr((int(ord(uncoded_string[sim])) + key_step))
#         print(int(ord(uncoded_string[sim])), coded_string)
# with open('yermolenko_oleksii_task5_output.txt', 'w') as output_file:
#      output_file.write(coded_string)

# # потом понял что этого мало и сделал так
# ВАРИАНТ 2
# with open('yermolenko_oleksii_task5_input.txt', 'r') as input_file:
#     uncoded_string = input_file.read()
#     key_step = int(input('please input step of krypto: '))
#     # print(uncoded_string)
#
#     text_len = len(uncoded_string)
#     coded_string = ""
#     for sim in range(0, text_len):
#         kod = ord(uncoded_string[sim])
#         if kod in range(1,47):
#             coded_string = coded_string + chr(int(kod))
#         elif kod in range(48, 57):
#             coded_string = coded_string + chr((int(kod) + key_step - 48) % 10 + 48)
#         elif kod in range(65, 91):
#             coded_string = coded_string + chr((int(kod) + key_step - 65) % 26 + 65)
#         elif kod in range(97, 123):
#             coded_string = coded_string + chr((int(kod) + key_step - 97) % 26 + 97)
#         elif kod in range(1040, 1072):
#             coded_string = coded_string + chr((int(kod) + key_step - 1040) % 32 + 1040)
#         elif kod in range(1072, 1104):
#             coded_string = coded_string + chr((int(kod) + key_step - 1072) % 32 + 1072)
#         else:
#             coded_string = coded_string + "*"
#             print(kod)
#
# with open('yermolenko_oleksii_task5_output.txt', 'w') as output_file:
#     output_file.write(coded_string)

# Но это решение тоже оказалоась не идеальным
# по символам в таблице 1105 и 1125 сдвиг на русской Ё ё и получается надо разбивать интервалы символов до и после Ё ё
# пока не придумал как реализовать







