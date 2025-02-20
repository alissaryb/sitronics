from flask import Flask, render_template, redirect

app = Flask(__name__)

courses = [{"id" : 0, "name_course" : "Вареники от алисой", "id_teacher" : 0, "address" : "Онлайн", "organization" : "МТС", "date_day" : "четверг", "time_start" : "10:00", "time_end" : "12:00", "price" : 300, "rank" : 9.5, "verified" : 1}, {"id" : 1, "name_course" : "Кулинарное кино", "id_teacher" : 1, "address" : "online", "organization" : "Sitronics", "date_day" : "пятница", "time_start" : "18:00", "time_end" : "20:00", "price" : 400, "rank" : 8.8, "verified" : 0}]

teachers = {0 : {"name" : "Алиса", "surname" : "Рыбакова", "patronymic" : "Ивановна"}, 1 : {"name" : "Михаил", "surname" : "Лавренов", "patronymic" : "Иванович"}}

def get_organization():
    set_organizations = set([course["organization"] for course in courses])
    all_organizations = list(set_organizations)
    return all_organizations

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html", title="")

@app.route('/cards', methods=['GET', 'POST'])
def cards():
    return render_template("cards.html", title="")

@app.route('/map', methods=['GET', 'POST'])
def cards():
    return render_template("map.html", title="")

@app.route('/check')
def check():
    names = ['Иванов Иван Иванович', 'Петров Петр Петрович', 'Сидоров Сидор Сидорович']
    educations = ['Московский государственный университет', 'Санкт-Петербургский государственный университет', 'Новосибирский государственный университет']
    ages = [30, 35, 40]

    teacher = {
        'name': random.choice(names),
        'age': random.choice(ages),
        'education': random.choice(educations),
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
