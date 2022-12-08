from collections import namedtuple

citizen = namedtuple("Житель", "имя возраст статус какую_группу_ты_уважаешь")
Alex = citizen(имя="Лёха Алексеев", возраст=27, статус="Предприниматель", какую_группу_ты_уважаешь="Аллу Пугачёву")

print(Alex.имя)
print(Alex.какую_группу_ты_уважаешь)
print(Alex)









