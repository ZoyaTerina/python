# try:
#     number = int(input("Введи число: "))
# except ValueError:
#     print("Понял")
# except IndexError:
#     print("Ы")
# else:
#     print("Понял2")
# finally:
#     print("я поработав")
#
#
# name = input("Введиимя друга(собаки): ")
# try:
#     if name == "Антон":
#         raise ValueError("Ты че, пёс")
# except ValueError as pelmeni:
#     print(pelmeni, "Запрещаю")

# 1 Задача
# def masha(content):
#     s = 0
#     k = 0
#     for chiclo in content:
#         try:
#             s += int(chiclo)
#         except ValueError:
#             print("Найдено не число:", chiclo)
#         else:
#             k += 1
#         if k == 0:
#             print("Чисел не было найдено.")
#             return "[Здесь ничего нет]"   # выход из функции
#     return round(s / k, 0)
# try:
#     g = open("23-02txt.py", "r", encoding="utf-8")
# except FileNotFoundError:
#     print("Файла нет, пока!")
#     quit()
# content = g.read().split()  # по пробелам и переному строки
# g.close()
# print(masha(content))

# 2 Задача
# try:
#     g = open("23-02txt.py", "r", encoding="utf-8")
# except FileNotFoundError:
#     print("Файла нет, пока!")
#     quit()
# content = g.readlines()
# g.close()
# print(content)
# for i, student in enumerate(content):
#     content[i] = student.split()
# maxi = -1
# for student in content:
#     try:
#         if int(student[3]) > maxi:
#             maxi = int(student[3])
#     except ValueError:
#         print("Неверно казаны баллы", student)
#     except IndexError:
#         print("Баллы отсутствуют", student)
# if maxi == -1:
#     print("Нет записей об участниках")
#     quit()
# print(maxi)


# 3 Задача
# try:
#     g = open("23-02txt.py", "r", encoding="utf-8")
# except FileNotFoundError:
#     print("Файла нет, пока!")
#     quit()
# content = g.read()
# word = input("Какое слово мы ищем: ")
# print(content.coint(word))












