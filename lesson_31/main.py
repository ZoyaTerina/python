from tkinter import *
root = Tk()
root.geometry("550x550")

# ========== Текст ==========
c = Canvas(root, width=250, height=250, bg="light blue")
c.pack(anchor=CENTER, expand=True)
#
# c.create_text(0, 0,
#               text="Пельмени * 8",
#               font="Arial 25",
#               fill="gold12",
#               anchor=NW)


# ========== Прямоугольник ==========
# c.create_rectangle(10, 10,
#                    200, 150,
#                    fill='red',
#                    width=10,
#                    outline='darkred')


# ========== Многоугольник ==========
# c.create_polygon(10, 10,
#                  50, 50,
#                  10, 50)


# ========== Окружность ==========
# c.create_oval(10, 120,
#               150, 90)


# ========== arc ==========
# c.create_oval(10, 10,
#               150, 150,
#               fill='yellow')
# c.create_arc(10, 10,
#              150, 150,
#              fill='gold',
#              start=35,      # точка начала
#              extent=-135,   # градусы
#              style=ARC,     # хорда
#              width=10)


# ========== Линии ==========
# c.create_line(10, 10,
#               150, 150,
#               arrow=BOTH,
#               arrowshape=(50, 50, 50),
#               width=10)


# =================================
# c.create_rectangle(10, 10,
#                    200, 150,
#                    fill='red',
#                    width=10,
#                    outline='darkred',
#                    dash="-.-",
#                    activefill="blue",
#                    activewidth=5)


root.mainloop()





























