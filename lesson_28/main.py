import tkinter as tk

def baget(event):
    print("да, я тот, кого знают как круасан")

window = tk.Tk()  # инициализация, создание В НАЧАЛЕ
window.geometry("500x400")  # размер окна
window.title("хлеб")

btn = tk.Button(window, text="хлеб")  # создание кнопки
btn.pack()  # размещение кнопки
btn['text'] = "А ты тоже круасан?"  # изменение конфигурации
btn['font'] = ("Arial Black",         # изменение шрифта
               15,
               "bold",  # жирный
               "underline",  # подчёркнутый
               "italic"  # курсив
               )
# btn['background'] = "pink"  # цвет фона
btn["bg"] = "pink"
# btn['foreground'] = "gold4"  # цвет текста
btn["fg"] = "white"
# btn['width'] = 10  # ширина
# btn['height'] = 3  # высота
# btn['borderwidth'] = 3  # ширина рамки
btn["bd"] = 3
# btn["command"] = baget  # нажатие левой кнопкой мыши
btn.bind("<Button-1>", baget)




window.mainloop()  # отоброжение окна В КОНЦЕ
































































