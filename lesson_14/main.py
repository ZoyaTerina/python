# # Первый Задача
# phrase = "Россия, Россия, Россия и Богдан".title().strip()
# symbols = list("!@#$%^&*();:?.,")
# phrase_clear = "" # помыли фразу
# for ovoshi in phrase:         # интерироваться по фразе
#     if ovoshi not in symbols:       # если это не спец. символ
#         phrase_clear += ovoshi
# phrase_list = phrase_clear.split(" ")
# d = {}
# for dom in phrase_list:
#     if dom not in d:
#         d[dom] = 1
#     else:
#         d[dom] += 1
# print(d)


# Второй задача
# sloj = 0
# d = {"Молоко": 100,
#      "Дошик": 21,
#      "Чипсы": 0.5,
#      "Богдан": 999}
# for i in d.values():     # перебор по значению
#     sloj += i
# print(sloj)


# Третий задача
# die_sides = 6
# die_count = 2
# d = {}
# for first in range(1, die_sides + 1):   # от 1 до 6 включительно
#     for second in range(1, die_sides + 1):
#         if first + second not in d: # если суммы  кубиков нет в словаре
#             d[first + second].append((first, second))
# for tadgikistan in d:
#     print(f"{tadgikistan}: {d[tadgikistan]}")





















































































