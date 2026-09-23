import random
import time


def get_day_name(day: int) -> str:
    match day:
        case 1:
            return "Понедельник"
        case 2:
            return "Вторник"
        case 3:
            return "Среда"
        case 4:
            return "Четверг"
        case 5:
            return "Пятница"
        case 6:
            return "Суббота"
        case 7:
            return "Воскресенье"
        case _:
            return "ОШИБКА: Неизвестный день недели"

print(get_day_name(3))
print(get_day_name(8))


def find_max_number():

    numbers = list(range(1, 10))
    max_number = numbers[0]

    for number in numbers:
        if number > max_number:
            max_number = number

    print(max_number)

find_max_number()


def stop_at_five():
    my_list = list(range(1, 8))

    for count in my_list:
        print(count)

        if count == 5:
            break

stop_at_five()


def create_strings():
    my_strings = [f"str{b}" for b in range(10)]
    print(my_strings)

create_strings()


def simulate_load():
    steps = 10
    warning_limit = 85
    pause_sec = 0.2

    for i in range(steps):
        load = random.randint(0, 100)

        if load > warning_limit:
            print(f"Высокая нагрузка: {load}")

        time.sleep(pause_sec)

simulate_load()
