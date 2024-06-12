from datetime import date, datetime
import csv


class Person:
    def __init__(self, surname, first_name, birth_date, nickname=None):
        self.surname = surname
        self.first_name = first_name
        self.nickname = nickname


        year, month, day = map(int, birth_date.split('-'))
        self.birth_date = date(year, month, day)

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year - (
                    (today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return str(age)

    def get_fullname(self):
        return f"{self.surname} {self.first_name}"


def create_csv_file(filename):

    data = [
        {"surname": "Smith", "first_name": "John", "birth_date": "1990-05-15", "nickname": "Johnny"},
        {"surname": "Doe", "first_name": "Jane", "birth_date": "1985-07-20", "nickname": "Janie"},
        {"surname": "Brown", "first_name": "Chris", "birth_date": "1975-02-10", "nickname": None}
    ]


    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['surname', 'first_name', 'birth_date', 'nickname']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in data:
            writer.writerow(row)

    print(f"Файл '{filename}' створено успішно.")


def modifier(filename):
    persons = []


    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            surname = row['surname']
            first_name = row['first_name']
            birth_date = row['birth_date']
            nickname = row.get('nickname', None)
            person = Person(surname, first_name, birth_date, nickname)
            persons.append(person)


    with open(filename, 'w', newline='') as csvfile:
        fieldnames = reader.fieldnames + ['fullname', 'age']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for person in persons:
            row = {
                'surname': person.surname,
                'first_name': person.first_name,
                'birth_date': person.birth_date.strftime('%Y-%m-%d'),
                'nickname': person.nickname,
                'fullname': person.get_fullname(),
                'age': person.get_age()
            }
            writer.writerow(row)


# Створення файлу
create_csv_file('contacts.csv')

# Модифікація файлу
modifier('contacts.csv')




