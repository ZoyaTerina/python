import tkinter as tk  # 1) импорт

root = tk.Tk()  # Создать окно
root.geometry("500x500")

# ======CHECKBUTTON======
# def check():
#     print(val_cb.get())
#
#
# val_cb = tk.BooleanVar()  # переменная для хранения True/False
# cb = tk.Checkbutton(root,
#                     text="подписка",
#                     font=15,
#                     bg="pink",
#                     variable=val_cb,  # хранение значения в ...
#                     onvalue=True,
#                     offvalue=False,
#                     command=check
#                     )  # создали переключатель
# cb.pack()
#
# root.mainloop()  # Отобразить окно


# ======RADIOBUTTON======
# def get_rb():
#     print(val_rb.get())
#
# val_rb = tk.IntVar()
# rb = tk.Radiobutton(root,
#                     text="Я почему то РАДИОкнопка",
#                     variable=val_rb,
#                     value=123,
#                     command=get_rb)
# rb.pack()
# rb1 = tk.Radiobutton(root,
#                     text="Я почему то РАДИОкнопка",
#                     variable=val_rb,
#                     value=0,
#                     command=get_rb)
# rb1.pack()
# root.mainloop()


# ======SCALE======
#
# def get_skala(lolkek):
#     # print(skala.get())
#     print(lolkek)
#
# skala=tk.Scale(root,
#                from_=500,  # откудова
#                to=1000,  # докудова
#                width=50,  # толщина полоски
#                length=300,  # длина полоски
#                orient=tk.HORIZONTAL,  # ориентация(север)
#                tickinterval=100,  # подпись
#                resolution=50,  # шаг
#                command=get_skala
#                )
# skala.pack()
#
# root.mainloop()


# ======КАРТИНКИ======
# img = tk.PhotoImage(file="1.png")  # объект изображения
# # img = img.subsample(3, 3)  # уменьшение
# # img = img.zoom(3, 3)  # увеличение
# lab = tk.Label(root, image=img)
# lab.pack()
#
# root.mainloop()


# ======СОСТОЯНИЕ======
#
# def switch():
#     if btn1['state'] == "disabled":  # если неактивна
#         btn1['state'] = "normal"
#     else:
#         btn1['state'] = "disabled"
#
# btn1 = tk.Button(root,
#                  text="Активируй меня",
#                  state=tk.DISABLED,
#                  fg="red",
#                  disabledforeground="grey80",
#                  width=30)
# btn1.pack(pady=20, ipady=20)
# btn2 = tk.Button(root,
#                  text="Активатор2023_без_вирусов",
#                  command=switch,
#                  width=30)
# btn2.pack()
#
#
# root.mainloop()


# ======ЗНАЧЕНИЕ ПО УМОЛЧАНИЮ======
ent = tk.Entry(root)
ent.pack()
ent.insert(tk.END, "перекус таксиста...")

root.mainloop()




