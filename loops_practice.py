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


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def print_car_info(self):
        print(f"{self.brand} {self.model} {self.year}")

car1 = Car("BMW", "X5", 2023)
car2 = Car("Toyota", "Camry", 2020)
car3 = Car("Honda", "Civic", 2019)

car1.print_car_info()
car2.print_car_info()
car3.print_car_info()


class Lead:
    def __init__(self, name):
        self.name = name

def change_name(lead, new_name):
    lead.name = new_name

lead = Lead("Danil")

print(lead.name)

change_name(lead, "Polikarp")  # в функцию change_name передаем тот же объект Lead, а не его копию. Функция меняет значение файла name

print(lead.name)


# Дальше задачки для закрепления. Конец отмечу так-же через коммент:

# class User:
#     def __init__(self, status):
#         self.status = status
#
# def change_status(user, new_status):
#     user.status = new_status
#
# user1 = User(status = "Offline")
# print(user1.status)
# change_status(user1, "Online")
# print(user1.status)

# закрепил задачкой выше, далее задача из карточки

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def get_avg_grades(self):
        if len(self.grades) == 0:
            return 0

        return sum(self.grades) / len(self.grades)

student1 = Student("Danil", 35, [5, 4, 3, 5])
student2 = Student("Polikarp", 54, [])

print(student1.get_avg_grades())
print(student2.get_avg_grades())

# для закрепления

# class Book:
#     def __init__(self, title, pages, ratings):
#         self.title = title  # название книги
#         self.pages = pages  # кол-во страниц
#         self.ratings = ratings  # список оценок, например [4, 5, 3, 2]
#
#     def get_avg_rating(self):
#         if len(self.ratings) == 0:
#             return 0
#         return sum(self.ratings) / len(self.ratings)
#
# book1 = Book('Пепел империума', 1489, [10, 9, 1, 5, 8])
# book2 = Book('Лживые боги', 2281, [])
#
# print(book1.get_avg_rating())
# print(book2.get_avg_rating())

# закрпеил, дём далее

student3 = Student("Alex", 21, [5, 5, 4, 5])
student4 = Student("Masha", 19, [4, 4, 4, 4])

students = [student1, student2, student3, student4]

grade_limit = 4.1

good_students = [
    current_student
    for current_student in students
    if current_student.get_avg_grades() > grade_limit
]

student_names = [
    selected_student.name
    for selected_student in good_students
]



print(student_names)




