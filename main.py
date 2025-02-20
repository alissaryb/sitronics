from flask import Flask, render_template, redirect
from random import choice

app = Flask(__name__)

def get_courses():
    return [
        {"id" : 0, "name_course" : "Введение в SQL", "id_teacher" : 0, "address" : "", 
         "type_online" : 1, "organization" : "МТС", "date_day" : "Четверг", "time_start" : "10:00", "time_end" : "12:00", "price" : 300, "rank" : 9.5, "verified" : 1}, 
         {"id" : 1, "name_course" : "Мужики кончают в рот негритянке", "id_teacher" : 1, "address" : "24 Minin Street, Building 1, Nizhny Novgorod, Russia", "type_online": 0,  "organization" : "Sitronics", "date_day" : "Пятница", "time_start" : "18:00", "time_end" : "20:00", "price" : 400, "rank" : 8.8, "verified" : 0}, 
         {"id" : 2, "name_course": "Искусственный интеллект", "id_teacher" : 2, "address" : "260 Maxim Gorky Street, Office 27, 4th Floor, Nizhny Novgorod, Russia", "organization" : "Sinergia", "date_day": "Вторник", "time_start" : "14:30", "time_end" : "17:30", "price": 750, "rank" : 4.5, "verified" : 1}, 
         {"id" : 3, "name_course": "Веб разработка", "id_teacher" : 3, "address" : "68 Karl Marx Street, Kazan, Republic of Tatarstan, Russia", "organization" : "T-bank", "date_day": "Суббота", "time_start" : "16:40", "time_end" : "17:40", "price": 900, "rank" : 2.5, "verified" : 0}]
def get_teachers():
    return {0 : {"name" : "Алиса", "surname" : "Рыбакова", "patronymic" : "Ивановна"}, 1 : {"name" : "Михаил", "surname" : "Лавренов", "patronymic" : "Иванович"}}

def get_organization():
    courses = get_courses()
    set_organizations = set([course["organization"] for course in courses])
    all_organizations = list(set_organizations)
    return all_organizations

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html", title="")

@app.route('/cards', methods=['GET', 'POST'])
def cards():
    return render_template("cards.html", title="")

@app.route('/courses', methods=['GET', 'POST'])
def courses():
    organizations = get_organization()
    return render_template("courses.html", title="", courses=get_courses(), teachers=get_teachers(), organizations=organizations)


@app.route('/map', methods=['GET', 'POST'])
def map():
    return render_template("map.html", title="")

@app.route('/check')
def check():
    names = ['Иванов Иван Иванович', 'Петров Петр Петрович', 'Сидоров Сидор Сидорович']
    educations = ['Московский государственный университет', 'Санкт-Петербургский государственный университет', 'Новосибирский государственный университет']
    ages = [30, 35, 40]

    teacher = {
        'name': choice(names),
        'age': choice(ages),
        'education': choice(educations),
        'photo': 'static/images/teacher.jpg',
        'confirmation_process': (
            "1. Проведение открытых уроков.\n"
            "2. Оценка отзывов студентов.\n"
            "3. Регулярные аттестации.\n"
            "4. Участие в профессиональных конкурсах."
        )
    }
    return render_template('check.html', teacher=teacher)

@app.route('/feedback')
def feedback():
    ratings = [10, 20, 30, 25, 15]  # Количество отзывов по звёздам
    total_reviews = sum(ratings)  # Общее количество отзывов
    return render_template('feedback.html', ratings=ratings, total_reviews=total_reviews)

if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1', threaded=True)
