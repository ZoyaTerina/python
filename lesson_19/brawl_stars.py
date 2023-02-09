import easygui
import random

def rock_paper_scissors():
    otvets = {"bumaga": "img/sas.png",
              "noznica":"img/dis",
              "kamen":"img/bymaga.png"}
    result = easygui.buttonbox(
        msg="выбери фигурку",
        title="А4, камэн, скала",
        image=["img/noznica.png", "img/bymaga.png", "img/sas.png"],
        choices=("Скала", "ножница", "A4")

    )
    print(otvets.keys())
    # answer_comp = random.chice(list(otvets.keys()))
    answer_comp = "noznica"
    print(answer_comp)
    if result == otvets["kamen"] and answer_comp == "noznica":
        easygui.msgbox(msg="Ура победа")
    # ДОСААААААТЬ, ПОНЯЛ???
def guess_the_number():
    n = easygui.integerbox(msg='Какое число?',
                       lowerbound=1,
                       upperbound=99)
    n_c = random.randint(1, 99)
    if n == n_c:
        return # выход из функции
    while n != n_c:
        if n > n_c:
            n = easygui.integerbox(msg='Какое число?',
                        lowerbound=1,
                        upperbound=99,
                                   image='img/БОЛЬШЕ.png')
games = [
    'Камень, ножницы, бумага',
    'Угадай число'
]

games_entry_points = [
    rock_paper_scissors,
    guess_the_number
]

while True:
    res = easygui.buttonbox('Выбери игру!', choices=games)
    if res is None:
        break
    games_entry_points[games.index(res)]()


























































