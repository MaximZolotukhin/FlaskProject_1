from flask import Flask, render_template, url_for, request
from data import title, subtitle, description, departures, tours
import os

app = Flask(__name__)
dep_page = ''

# @app.errorhandler(404)
# def render_error_page(error):
#     return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!", error

#Главная страница
@app.route('/')
@app.route('/index/')
def render_index():
    tours_index_page = []
    for count, value in tours.items():
        if count < 7:
            tours_index_page.append(value)
        else:
            break

    return render_template('index.html', title=title, subtitle=subtitle, description=description, departures=departures, tours=tours)

#Вьюха страницы туры
@app.route('/departure/<depart>') #<str:depar> Динамически предающаяся часть страницы
def render_departure(depart): #Параметр для дальнейшей работы в вьюхе
    tours_index_page = []
    for count, value in tours.items():
        tours_index_page.append(value)
    print(tours_index_page)

    return render_template('departure.html', description=description, departures=departures, tours=tours, departure=depart, tour_doct=tours_index_page)
    #depar=depar передаю переменну в шаблон для отрисовки только нужных данных

@app.route('/tour/<int:id>') #<str:depar> Динамически предающаяся часть страницы
def render_tour(id): #Переменная для фильтарции
    return render_template('tour.html', departures=departures, tours=tours, id=id)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
