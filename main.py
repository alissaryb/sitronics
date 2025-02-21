from flask import Flask, render_template, redirect
from random import choice

app = Flask(__name__)

def get_courses():
    return [
        {"id" : 0, "name_course" : "Введение в SQL", "id_teacher" : 0, "address" : "", "coords": "", "type_online" : 1, "organization" : "МТС", "date_day" : "Четверг", "time_start" : "10:00", "time_end" : "12:00", "price" : 300, "rank" : 9.5, "verified" : 1},
         {"id" : 1, "name_course" : "Вокал", "id_teacher" : 1, "address" : "24 Minin Street, Building 1, Nizhny Novgorod, Russia", "coords": [56.326552, 44.024662], "type_online": 0,  "organization" : "Sitronics", "date_day" : "Пятница", "time_start" : "18:00", "time_end" : "20:00", "price" : 400, "rank" : 8.8, "verified" : 0},
         {"id" : 2, "name_course": "AI с нуля", "id_teacher" : 0, "address" : "260 Maxim Gorky Street, Office 27, 4th Floor, Nizhny Novgorod, Russia", "coords": [56.322005, 44.032550], "type_online": 0, "organization" : "Sinergia", "date_day": "Вторник", "time_start" : "14:30", "time_end" : "17:30", "price": 750, "rank" : 4.5, "verified" : 1},
         {"id" : 3, "name_course": "Веб-разработка", "id_teacher" : 1, "address" : "68 Karl Marx Street, Kazan, Republic of Tatarstan, Russia",  "coords": [55.7943607, 49.13753724120586], "type_online": 0,"organization" : "T-bank", "date_day": "Суббота", "time_start" : "16:40", "time_end" : "17:40", "price": 900, "rank" : 2.5, "verified" : 0},
    {"id" : 4, "name_course": "Физический эксперементариум ", "id_teacher" : 2, "address" : "3 Lenin Square, Republic of Mari El, Russia",  "coords": [56.630733, 47.892071], "type_online": 0,"organization" : "Volga Region University", "date_day": "Пятница", "time_start" : "15:00", "time_end" : "17:00", "price": 10000, "rank" : 1.5, "verified" : 0}]
def get_teachers():
    return {0 : {"name" : "Алиса", "surname" : "Рыбакова", "patronymic" : "Ивановна"}, 1 : {"name" : "Михаил", "surname" : "Лавренов", "patronymic" : "Иванович"}, 2 : {"name" : "Кирилл", "surname" : "Фёдоров", "patronymic" : "Математика"}}

def get_repetitors():
    return [
    {"id" : 0, "name" : "Бернштейн Лев Евгеньевич", "age" : 45, "education": "НИУ ВШЭ", "coll_deg" : 1, "mail" : "bernshtein@mail.ru"},
    {"id" : 1, "name" : "Рыбакова Алиса Сергеевна", "age" : 52, "education": "Синергия", "coll_deg" : 0, "mail" : "alisa@mail.ru"  },
    {"id" : 2, "name" : "Брусенцев Александр Петрович", "age" : 69, "education": "МФТИ", "coll_deg" : 1, "mail" : "brusntsev@mail.ru"  },
    {"id" : 3, "name" : "Амирханян Михаил Александрович", "age" : 28, "education": "МГУ", "coll_deg" : 0, "mail" : "amirihan@mail.ru"   }
    ]

def get_companies():
    return [
        {'name': 'МТС Диджитал', 'post': 'Junior Developer', 'rank' : 'Кандитат в мастера', 'link' : 'https://mts-digital.ru/'}, 
        {'name': 'T-bank', 'post': 'Intern Software Engineer', 'rank' : 'Мастер', 'link' : 'https://education.tbank.ru/start/'}, 
        {'name': 'Sitronics Group', 'post': 'Data Analyst Intern', 'rank' : 'Эксперт', 'link' : 'https://www.sitronics.com/businesses'}, 
        {'name': 'VK Tech', 'post': 'Machine Learning Intern', 'rank' : 'Мастер', 'link' : 'https://tech.vk.com/'}, 
        {'name': 'Ростех', 'post': 'Frontend Developer Intern', 'rank' : 'Кандитат в мастера', 'link' : 'https://rostec.ru/careers/'}, 
        {'name': 'СИГМА', 'post': 'Security Analysis Intern', 'rank' : 'Специалист', 'link' : 'https://sigma-it.ru/'}
        ]

def get_organization():
    courses = get_courses()
    set_organizations = set([course["organization"] for course in courses])
    all_organizations = list(set_organizations)
    return all_organizations

def get_info_map():
    cities = []
    for i in get_courses():
        if i['type_online'] == 0:
            sl = {}
            sl['id'] = i['id']
            sl['name'] = i['name_course']
            sl['coords'] = i['coords']
            cities.append(sl)
    return cities

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html", title="")

@app.route('/courses', methods=['GET', 'POST'])
def courses():
    organizations = get_organization()
    return render_template("courses.html", title="", courses=get_courses(), teachers=get_teachers(), organizations=organizations)


@app.route('/map', methods=['GET', 'POST'])
def map():
    cities = get_info_map()
    print(cities)
    return render_template("map.html", title="", cities=cities)

@app.route('/page_course/<cour_id>', methods=['GET', 'POST'])
def page_course(cour_id):
    cour = {}
    print(cour_id, type(cour_id))

    for i in get_courses():
        if int(cour_id) == i['id']:
            cour = i
            break

    teachs = get_teachers()
    print(teachs)
    print(int(cour['id_teacher']))
    teach = teachs[int(cour['id_teacher'])]
    return render_template("page_course.html", title="", cour=cour, teach=teach)

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('signup.html')

@app.route('/repetitors')
def repetitors():
    teacher = get_teachers()
    return render_template('repetitors.html', teacher=teacher)


@app.route('/account')
def account():
    teacher = get_teachers()
    return render_template('account.html', teacher=teacher)


@app.route('/repetitor/<rep_id>')
def repetitor(rep_id):
    teachers = get_teachers()
    teacher = teachers[int(rep_id)]
    return render_template('check.html', teacher=teacher)

@app.route('/internships')
def internship():
    companies = get_companies()
    return render_template('internship.html' , companies=companies)


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1', threaded=True)
