# # Функции
# def functia(x):     # объявление функции
#     return x + 1
#
# print(functia(5))     # вызов функциии с аргументом
#
# f = lambda x2: x2 + 1    # объявление лямбда функции
# print((5))    # вызов ляиюда функции


# # Фа соль
#
# beans = 20
# def vichitanie(x):
#     global beans
#     beans -= x
#
# while beans > 0:
#     while True:    # Валидация(НЕ ТРОГАТЬ)
#         first = int(input("Первый игрок сколько фа соли взять : "))
#         if first < 4 and first > 0:
#             break
#     vichitanie(first)
#     print(beans)
#     if beans <= 0:
#         print("========== ПОБЕДИЛ ВТОРОЙ ИГРОК ==========")
#         break
#     vichitanie(vtoroi)
#     print(beans)
#     while True:    # Валидация(НЕ ТРОГАТЬ)
#         vtoroi = int(input("Первый игрок сколько фа соли взять : "))
#             if vtoroi < 4 and vtoroi > 0:
#                 break
#     vichitanie(vtoroi)
#     print(beans)


# # Таймер
# from random import randint
# import time
# print("Время проверить твою ловкость и скорость")
# input("Нажми Enter чтобы начать")
# print("Время пострелять")
# time.sleep(randint(2, 5))
# start = time.time()
# print("СРЕЛЯЙ !!!")
# end = time.time()
# delta = end-start
# print(delta)
# if delta > 0.3:
#     print("Ты медленная черепаха!! стреляй быстрее!!")
# elif delta < 0.01:
#     print("Ты слишком быстрый ")
# else:
#     print("Аааа, успел среагировать, я то думал...")




















































