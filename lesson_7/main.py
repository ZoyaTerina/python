# ZeroDivisionError: division by zero - ошибка деления на ноль
#x = 5/0

#TypeError: can only concatenate str (not "int") to str - нельзя плюсовать строчки и цифры
#x = "а" + 15

#IndexError: list index out of range - ты вышел за приделы списка
#x = [0, -15, "Антон"]
#x[3]
#SyntaxError: unterminated string literal - не закрыта кавычка
#x = "Привет, я Антон.
#SyntaxError: expected ':' - забыто двоиточие
#if 5 == 4
#    print()
#
# NameError: name 'x2' is not defined
# x = "Я строчка"
# print(x2)

# assert --> AssertionError
# def summa(numbers):
#     return sum(numbers)
#
# print(summa([3,4]))
#
# assert summa([1,2]) == 3
# assert summa([1,2]) == 4


# try - попытаться
# except - отлавливание ошибок
# else - иначе, если ошибок не было (если всё хорошо)
# finally  -  закончить
# try:
#     number = int(input())
#     x = 5 / number
# except ZeroDivisionError:
#     print("Слышь ты, нельзя на нуль делить😈")
# except ValueError:
#     print("Хочу цифирки")
# except Exception:    # любая ошибка будет обработана
#     print("Блин, ты обшибибся, получается")
# else:   # else - когда всё хорошо🤗
#     print("Я поделив 👉👈")
# finally:
#     print("Меня написал Антон. Все права защищены.")
# print("Я закончил работать.")




# PASS
# try:
#     number = int(input())
#     x = 5 / number
# except Exception:
#     pass  # pass - это затычка, ничего не произойдет.


# if 5 == 5:
#     pass    # TODO: купить молоко и дописать код
#

try:
    x = input("Введи имя: ")
    if x == "Антон":
        raise Exception ("Антона в обиду не дам")
        # raise - вызвать искулючение или ошибку
except Exception as error_massage:
    # as - сохранить ошибку в error_massage
    print("Это слово запрещено!")



























































