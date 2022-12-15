# МНОЖЕСТВА

# s = set() #пустое множество
# s1 = {1, 2, 3}      # дубликаты исключаются( повторения )
# print(s1)


# s2 = {"A", "B", "C"}    # не упорядоченный тип данных
# print(s2)


# s1 = {1, 2, 3, 4, 5}
# s2 = {7, 6, 5, 4, 3}
# print(s1.union(s2))         # объединение
# print(s1| s2)               # объединение
#
# print(s1.intersection(s2))  # пересечение
# print(s1 & s2)              # пересечение
#
# print(s1.difference(s2))    # разность
# print(s1 - s2)              # разность
#
# print(s1.symmetric_difference(s2))     # симметрическая разность
# print(s1 ^ s2)                         # симметрическая разность


# СЛОВАРИ
# d = {}     # пустой словарь
# d1 = {"Пи": 3.14,
#       "Преподаватель": "Антон",
#       "Список дел": ["выжить", "ловить балдёж"],
#       "Словарь": {"Вл1": 1}}
# print(d1["Преподаватель"])        # Антон
# print(d1["Список дел"][1])        # Ловить балдёж
# print(d1["Словарь"]["Вл1"])       # 1



# from random import randint
# lst = []
# for _ in range(5):
#     lst.append(randint(1, 5))
# print(lst)
# unique = set(lst)
# print(unique)
# print(f"{len(unique)} штук: {unique}")

# from random import randint
# lst1 = []
# lst2 = []
# size = randint(100, 1000)
# r_start = 0
# r_end = 10_000   # _ - декоративный разделитель
# for _ in range(size):
#     lst1.append(randint(r_start, r_end))
#     lst2.append(randint(r_start, r_end))
# set1 = set(lst1)
# set2 = set(lst2)
# inter = set1.intersection(set2)
# print(f"Общих чисел: {len(inter)}")
# print(f"[Кол-во генераций]: {size}")
# print(f"[Максимальное значение]: {max(inter)}")
# print(f"[Минимальное значение]: {min(inter)}")
# # # озможное решение, но колхозное
# # inter1 = list(inter)
# # inter1.sort()
# # print(inter1)
# # # интелектуальное решение
# print(sorted())     # sorted() - сортерует + преобразование в список

# set1 = set()
# insert = ""
# while insert != "end":
#     insert = input("Ввод: ")
#     if insert.lstrip("-").isdigit():        # если это число
#         if insert not in set1:  # если числа не было
#             print("❌ НЕТ")
#             set1.add(insert)
#         else:
#             print("✅ ДА")
#     elif insert == "end":
#         break
#     else:
#         print("⛔ Число хочу. И шашалычка бы щас, кст.")











































































