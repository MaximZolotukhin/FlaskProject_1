from flask import Flask, render_template, url_for
from data import title, subtitle, description, departures, tours
import os

app = Flask(__name__)


#Главная страница
@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html', title=title, subtitle=subtitle, description=description, departures=departures, tours=tours)
#
#
# #Направления
# @app.route('/departures/<departure>/')
# def departures(departure):
#     return render_template('departure.html', title=title)
#
# #Туры
# @app.route('/tours/<id>')
# def tours(id):
#     return render_template('tour.html', title=title)
#
# @app.route('/data/')
# def data():
#     return render_template('data.html')
#
# @app.route('/data/departures/<departure>/')
# def data_departure(departure):
#     return render_template('data.html', departure=departure)
#
# @app.route('/data/tours/<id>/')
# def data_tours(id):
#     return render_template('cuba.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
