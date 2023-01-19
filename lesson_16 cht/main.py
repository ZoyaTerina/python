# def plus_one(a, b):         # объявление функции с 2 аргументами
#     return a + b + 1
#
# print(plus_one(5, 4))


# ЛЯМБДА ФУНКЦИИ
# plus_one = lambda a, b: a + b + 1
# print(plus_one2(5, 2))

# if-else в lambda
# result = lambda answer: True if answer == "Д" else False

# List comprehension  (генератор списка)
# spisok = []
# for i in range(1, 6)     # от 1 до 5
#     spisok.append(i)
# print(spisok)
#
# spisok2 = [n for n on range(1, 6)]
# # 1. List comprehension всегда пишется в []
# # 2. for n in range(1, 6)   обычный цикл for -> сколько будет элементов в списке
# # 3. все что слева от for -> элемент списка
# print(spisok2)

# первый задача
# c2f = lambda c: c * 9/5 + 32
# f2c = lambda f:(f - 32) * 5/9
# c2k = lambda c: c + 273.15
# k2c = lambda k: k - 273.15
# f2k = lambda f: c2k(f2c(f))
# print(f2k(203))

# второй задача
from random import randint
# arbuz = int(input('слыш банан сколько раз бросиш неокуб'))
# banana = lambda zxc: True if zxc == "де" else False
# while True
# dies = [randint(1, 6) for n in range(arbuz)]
# print(dies)
# kivi = input("выхоишь лы ти? де/нат").upper()
# bananа(kivi)
# if banana(kivi):       # если игрок решил выйти

# Третий задача
# from random import choice
# chars = [list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"),
#          list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя"),
#          list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
#          list("abcdefghijklmnopqrstuvwxyz"),
#          list("1234567890")
#         ]
# cot = [choice(choice(chars)) for n in range(6)]
# cotik = "".join(cot)
# dictionarry = {}
# ssylka_na_kavkaz = "https://www.google.com"
# if ssylka_na_kavkaz in dictionarry:
#     print("ссылка уже есть в базе, вот кот:")
#     print(dictionarry[ssylka_na_kavkaz])    #выводим код ссылки
# else:
#     print("ссылка добавлена, держи кота:")
#
# Четвёртый за особняком
# u = lambda a, b b:a / b
# print(u(6, 3))
# u2 = lambda a, b:a % b
# print(u2(6, 3))
# u3 = lambda a, b:a // b
# print(u3(6, 3))
# u4 = lambda a, b:a**b
# print(u4(6, 3))
# u5 = lambda a:-a if a < 0 else a # если отрицательное число меняем знак
# print(u5(-6))
















































