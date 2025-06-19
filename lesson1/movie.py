movie = []
while True:
    menu = """""
        1. Додати до списку
        2. Видалити  зі списку
        3. Переглянути список
    """""
    print(menu)
    answer = input()

    if answer == "1":
        do = input("Що додати до списку? ")
        movie.append(do)
        print(movie)
    elif answer == "2":
        delete = input("Що видалити зі списку? ")
        movie.remove(delete)
        print(movie)
    elif answer == "3":
        print(movie)