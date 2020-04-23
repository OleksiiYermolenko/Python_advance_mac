
#  Version 1_Lazzy
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

# # 1105 и 1125 сдвиг на русской Ё ё и получается надо разбивать интервалы символов до и после Ё ё
# пока не придумал как реализовать
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
