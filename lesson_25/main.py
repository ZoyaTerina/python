# class Chelovek:
#     pi = 3.14   # public статический
#     __city = "Новосибирск"  # private статический
#     def __init__(self, height):
#         self.hi = 188       # public динамический
#         self.__vozrast = 40 # private динамический
#
# obj = Chelovek(177)
# print(obj.hi)
# print(obj.pi)
# # print(Chelovek.pi)

# class Chelovek:
#     def __init__(self, height):
#         self.hi = height
#
# obj = Chelovek()   # не передал -> по умолчанию
# print(obj.hi)
#
# obj2 = Chelovek(150)   # передал -> переданный аргумент
# print(obj2.hi)


# import random
# class Human:
#     default_name = "Oleg"
#     default_age = 98
#     def __init__(self, name=default_name, age=default_age):
#         self.name = name
#         self.age = age
#         self.__money = 10_000
#         self.__house = None
#     def info(self):
#         return self.age, self.name, self.__money, self.__house
#     def earn_money(self):
#         self.__money += 190_000
#     def default_info(self):
#         return Human.default_name, Human.default_age
#     def __make_deal(self, dom):
#         if self.__money > dom.final_price():
#             self.__money -= dom.final_price()
#             print("Денег достаточно")
#             return True
#         else:
#             return False
#     def buy_house(self, dom):
#         if self.__make_deal(dom):
#             return "Хата приобретена"
#             dom.owner = self.name
#             self.__house = dom
#         else:
#             return f"У тебя: {self.__money}, нужно: {House.self.__price}"
#
# class House:
#     def __init__(self, ar="Сочи", pr=15_000):
#         self.__area = ar
#         self.__price = pr
#         self.__skidka = random.randint(5, 25)
#     def final_price(self):
#         return self.__price - self.__price * self.__skidka
#
#
# anton = Human()
# dom1 = House()
#
# anton.buy_house(dom1)











































