# class Nazvanie:
#     def __init__(self):  # magic метод
#         self.money = 1_000   # public
#         self.__zarplata = 3   # private
#     def bar(self):  # public метод
#         if self.__zarplata > 4:   #
#             return True
#         else:
#             self.__sad()   # вызов private метод
#             return False
#
#     def __sad(self):  # private метод
#         print("*Сане грустно*")
#
# sanya = Nazvanie()
# print(sanya.money)  # public выводить
# sanya.money += 100  # public можно менять
# # print(sanya.__zarplata)   # private нельзя выводить
# # sanya.__zarplata = 10     # public
# # sanya.__zarplata += 10    # private ельзя изменять
# # print(sanya.__zarplata)
# print(sanya.bar())
#
# sanya._Nazvanie__zarplata = 1_000_000
# print(sanya.bar())


# Задача 1
# class Car:
#     def on(self, on):
#         print("Вкл")
#     def off(self, off):
#         print("Выкл")
#     def year(self, year):
#         self.year = year
#     def type(self, type):
#         self.type = type
#     def color(self, color):
#         self.color = color
#
# sanincar = Car()
# sanincar.color("Синий(чёрный)")
# print(sanincar.color)
# sanincar.type("Кроссовер")
# print(sanincar.type)
# sanincar.year(1991)
# print(sanincar.year)
# print(sanincar.on)
# print(sanincar.off)

# Задача 2
import string
# class Alphabet:
#     def __init__(self, lang):
#         self.__lang = lang
#         self.__letters = string.ascii_lowercase
#     def print(self):
#         print(self.__letters)
#     def letters_num(self):
#         print(len(self.__letters))
# al = Alphabet("eng")
# al.print()
# al.letters_num

# Задача 3
import string
import datetime


# class Nazvanie:
#     def __init__(self):  # magic метод
#         self.money = 1_000  # public
#         self.__zarplata = 3  # private
#
#     def bar(self):  # public метод
#         if self.__zarplata > 4:  # используем private
#             return True
#         else:
#             self.__sad()  # вызов private метода
#             return False
#
#     def __sad(self):  # private метод
#         print("*Сане грустно*")
#
#
# sanya = Nazvanie()
# # print(sanya.money)  # public можно выводить
# # sanya.money += 100  # public можно менять
#
# # print(sanya.__zarplata)  # private нельзя выводить
# # sanya.__zarplata = 10  # public
# # sanya.__zarplata += 10  # private нельзя изменять
# # print(sanya.__zarplata)
# print(sanya.bar())
#
# sanya._Nazvanie__zarplata = 1_000_000  # меняем private
# print(sanya.bar())


# 1 задача
# class Car:
#     def start(self):
#         return "Я(машина) завёлся"
#
#     def stop(self):
#         return "Я(машина) развёлся"
#
#     def c(self, color):
#         self.color = color
#
#     def y(self, year):
#         self.year = year
#
#     def t(self, type):
#         self.type = type
#
# anton = Car()
# anton.c("черный(синий)")
# print(anton.color)
# anton.t("бэчбэк")
# anton.y(1900)
# print(anton.start())
# print(anton.stop())

# задача2
# class Alphabet:
#     def __init__(self, lang):
#         self.__lang = lang
#         self.__letters = string.ascii_lowercase
#     def print(self):
#         print(self.__letters)
#     def letters_num(self):
#         print(len(self.__letters))
#
#
# al = Alphabet("eng")
# al.print()
# al.letters_num()

# задача 3
# import datetime
# class Clock:
#     def __init__(self):
#         # self.__time = datetime.datetime.now().strftime("%H:%M:%S")
#         self.__time = "08:07:06"
#         self.__h, self.__m, self.__s = self.__time.split(":")
#         self.__h, self.__m, self.__s = int(self.__h), int(self.__m), int(self.__s)
#
#     def hours(self):
#         self.__h += 1
#
#     def minutes(self):
#         self.__m += 1
#
#     def seconds(self):
#         self.__s += 1
#
#     def test_h(self):
#         if self.__h > 23:
#             self.__h = 0
#
#     def test_m(self):
#         if self.__m > 59:
#             self.__m = 0
#             self.__h += 1
#
#     def vivod(self):
#         print(f"{str(self.__h).rjust(2, '0')}:{str(self.__m).rjust(2, '0')}:{str(self.__s).rjust(2, '0')}")
#
#
# time_0 = Clock()
# time_0.minutes()
# # time_0.test_m()
# time_0.vivod()


























































