# Классы
# class Person:  # объявление класса
#     def __init__(self, imya, vozrast):  # метод инициализации
#         self.age = vozrast  # Установка значений атрибутов
#         self.name = imya
#     def __str__(self):
#         return ("Я Кристина")
#
# eugenii = Person("Юджин", 40)
# anna = Person(vozrast=0, imya="Кристина")
#
# print(anna.name)
# print(eugenii.age)
#
# print(anna)


# class HelloWorld:
#     def __getitem__(self, key):
#         print("hello world", key)
#
# hi = HelloWorld()
#
# # !!! обрати внимания, что здесь нет print(), просто обращение по ключу
# hi[12241412414]
# hi[21414]


# Задача 1
# class Person:
#     def __init__(self, imya, vozrast, familia):
#         self.name = imya
#         self.age = vozrast
#         self.f = familia
#     def __str__(self):
#         return f"{self.name}, {self.age}, {self.f}"
#     def greet(self):
#         return f"Привет! Я {self.name}, мне {self.age}, моя фамилия {self.f}"
# anna = Person("Аня", 20, "Петрова")
#
# print(anna.greet())
# print(anna.name)
# print(anna.age)
# print(anna.f)
# print(anna)


# Задача 2

# from random import randint
# class Person:
#     def __init__(self, imya, vozrast, familia):
#         self.name = imya
#         self.age = vozrast
#         self.f = familia
#         self.grates = [randint(2, 5) for n in range(randint(1, 6))]
#         self.sa = sum(self.grates) / len(self.grates)
#     def __str__(self):
#         return f"{self.name}, {self.age}, {self.f}"
#     def greet(self):
#         return f"Привет! Я {self.name}, мне {self.age}, моя фамилия {self.f}"
#
# anna = Person("Аня", 20, "Петрова")
# # print(anna.greet())
# # print(anna.name)
# # print(anna.age)
# # print(anna.f)
# # print(anna.grades)
# # print(anna.sa)
# melanya = Person("Мелаша", 13, "Дорн")
# vladislav = Person("Владик", 10, "Хых")
# anton = Person("Тоша", 1, "Смирнов")
# studen = [anna, melanya, vladislav, anton]
#
# dnevnik = {}
#
# for item in studen:
#     dnevnik[item.name] = item.sa
#
# print(dnevnik)
#
# print(dnevnik.items())
# sorted_dnevnik = dict(reversed(sorted(dnevnik.items(), key=lambda item: item[1])))
# print(sorted_dnevnik)
#
# schetchik = 0
# for item in sorted_dnevnik:
#     schetchik += 1
#     print(f"{schetchik}. {item} - {sorted_dnevnik[item]}")


# Задача 3

# class Rectangle:
#     def __init__(self, d1, d2):
#         self.dot1 = d1
#         self.dot2 = d2
#     def ploshad(self):
#         a = self.dot2.y - self.dot1.y
#         b = self.dot2.x - self.dot1.x
#         return a * b
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# dot1 = Point(1, 152)
# dot2 = Point(2, 250)
# prymoyg = Rectangle(dot1, dot2)
#
# print(prymoyg.ploshad())





























































