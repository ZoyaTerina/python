import tkinter as tk

# def show_message():
#     # приём значения из Entry
#     message = ent.get()  # получить значение с поля ввода
#     ent.delete(0, 'end')  # очистка поля для ввода полностью
#     lab['text'] = message
#     print(message)
#
#     # приём значения из Text
#     message2 = txt.get(2.4, 'end')  # отсчёт от 1.0
#     txt.delete(0.0, 'end')  # очистка Text
#     print(message2)
#
# window = tk.Tk()
# window.geometry("300x400")
# lab = tk.Label(window, text="Бублики",
#                font="Verdana 18",
#                bg="pink", fg="white",
#                width=50)  # надпись
# lab.pack()
# ent = tk.Entry(window, bd=7, width=10)  # поле для ввода
# ent.pack()
#
# btn = tk.Button(window, text="пожарить хлеб", bg="pink", fg="white", command=show_message)
# btn.pack()
#
# txt = tk.Text(window, width=20, height=5)  # многострочный ввод
# txt.pack()
#
# window.mainloop()


# def show_message():
#     message = ent.get()
#     ent.delete(0, 'end')
#     print(message)
#
#     message2 = txt.get(0.0, 'end')
#     txt.delete(0.0, 'end')
#     print(message2)
#
# window = tk.Tk()
# window.geometry("400x400")
# window.configure(background='lightblue')
#
#
# lab = tk.Label(window, text="ваш адрес:",
#                font="Verdana 18",
#                bg="lightblue", fg="white",
#                width=50)
# lab.pack()
# ent = tk.Entry(window, bd=10, width=20)
# ent.pack()
#
# lab = tk.Label(window, text="комментарий:",
#                font="Verdana 18",
#                bg="lightblue", fg="white",
#                width=50)
# lab.pack()
# txt = tk.Text(window, width=30, height=10)  # многострочный ввод
# txt.pack()
#
# btn = tk.Button(window, text="отправить", bg="lightblue", fg="white", command=show_message)
# btn.pack()
#
# window.mainloop()



window = tk.Tk()
window.geometry("400x400")

lab = tk.Label(window, text="цвет",
               font="Verdana 18",
               fg="black",
               width=50)
lab.pack()

btn = tk.Button(window, bg="red", bd=5, width=20)
btn.pack()
btn = tk.Button(window, bg="orange", bd=5, width=20)
btn.pack()
btn = tk.Button(window, bg="yellow", bd=5, width=20)
btn.pack()
btn = tk.Button(window, bg="green", bd=5, width=20)
btn.pack()
btn = tk.Button(window, bg="blue", bd=5, width=20)
btn.pack()
btn = tk.Button(window, bg="darkblue", bd=5, width=20)
btn.pack()
btn = tk.Button(window, bg="purple", bd=5, width=20)
btn.pack()


window.mainloop()











