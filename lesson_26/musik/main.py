from musicbox import MusicBox
a = MusicBox()  # плеер
while True:
    a.igraem()
    otvet = input("Что ты услышал? : ").upper()
    if otvet == " ":     # если ответ пустой
        break
    a.proverit(otvet)




































































