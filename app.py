from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

#Главная страница
@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

#Направления
@app.route('/departures/<departure>/')
def departures(departure):
    return 'Здесь будет направление'

#Туры
@app.route('/tours/<id>')
def tours(id):
    return 'Здесь будет тур'


if __name__ == '__main__':
    app.run(debug=True)
