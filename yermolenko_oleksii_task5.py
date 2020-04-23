
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
with open('yermolenko_oleksii_task5_output.txt', 'w') as output_file:
    coded_string = output_file.write()



# with open('yermolenko_oleksii_task5_input.txt', 'r') as input_file:
#     uncoded_string = input_file.read()
#     key_step = int(input('please input step of krypto: '))
#     print(uncoded_string)
#     text_len = len(uncoded_string)
#     coded_string = ""
#     for sim in range(0, text_len):
#         kod = ord(uncoded_string[sim])
#         if kod == 32:
#             coded_string = coded_string + " "
#         elif kod in range(48, 57):
#             if (kod + key_step) > 57:
#                 kod -= key_step
#                 coded_string = coded_string + chr((int(kod) + key_step))
#             else:
#                 coded_string = coded_string + chr((int(kod) + key_step))
#
#         elif kod in range(65, 90):
#             if (kod + key_step) > 90:
#                 kod -= key_step
#                 coded_string = coded_string + chr((int(kod) + key_step))
#             else:
#                 coded_string = coded_string + chr((int(kod) + key_step))
#
#         elif kod in range(97, 122):
#             if (kod + key_step) > 122:
#                 kod -= key_step
#                 coded_string = coded_string + chr((int(kod) + key_step))
#             else:
#                 coded_string = coded_string + chr((int(kod) + key_step))
#
#         elif kod in range(1040, 1071):
#             if (kod + key_step) > 1071:
#                 kod -= key_step
#                 coded_string = coded_string + chr((int(kod) + key_step))
#             else:
#                 coded_string = coded_string + chr((int(kod) + key_step))
#
#         elif kod in range(1072, 1103):
#             if (kod + key_step) > 1103:
#                 kod -= key_step
#                 coded_string = coded_string + chr((int(kod) + key_step))
#             else:
#                 coded_string = coded_string + chr((int(kod) + key_step))
#
#     print(coded_string)

# for sim in range(0, 96):
#     coded_string2 = chr(sim)
#     print(sim, coded_string2)

# 32 пробел
# 48-57
# 65-90 лат больш
# 97-122 лат мал
# 1040-1071 кир больш
# 1072-1103 кир мал



# coded_string2 = ""
# for sim in range(0, text_len):
#     coded_string2 = coded_string2 + chr((int(ord(coded_string[sim])) - key_step))
# print(coded_string2)
#
#
# АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ
