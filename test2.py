# 6 Дан файл с текстом, вывесли список который содержит все имена,
# все фамилии и все географические названия.
# Имена, Фамилии и Географические названии в простом формате, без дифисов.
import csv
from re import findall
import requests
import urllib.request

# def finder_all(file):
#     numb_sum = 0
#     with open(file) as text:
#         text_start = text.read()
#         text_found = findall(r"\d+\.\d+|-\d+\.\d+|\d+|-\d+", text_start)
#         for item, elem in enumerate(text_found):
#             text_found[item] = float(elem)
#             numb_sum = numb_sum + text_found[item]
#         print(text_found, numb_sum)
#
#
# def csv_match():
#     find = finder_all()
#     pass

# def reqest_surname(surname):
#
#     t = requests.get('https://ridni.org/karta/', params=surname)
#     # t = urllib.request.urlopen('https://ridni.org/karta/' + surname)
#
#     # print ("result code: " + str(t.getcode()))
#
#     print(t)
#
#
# reqest_surname('Пет')
# #
#
# # В этом и всех последующих ДЗ можно использовать все библиотеки которые доступны в Python
#
# no_negative_number()


from bs4 import BeautifulSoup
import requests
import urllib.request
from urllib import urlopen

# import
html_doc = urllib.request.urlopen('http://otus.ru').read()

soup = BeautifulSoup(html_doc)
print(soup)
