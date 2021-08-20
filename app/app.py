from typing import List, Dict
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import json

app = Flask(__name__)

config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'tddflask'
    }


def add_data(name, color):
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    try:
        query = 'INSERT INTO favorite_colors (name, color) VALUES (%s, %s)'
        val = (name, color)
        cursor.execute(query, val)
        connection.commit()
    except:
        print("primary key error")
    cursor.close()
    connection.close()

    return True


def get_data() -> List[Dict]:
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM favorite_colors')
    results = [{name: color} for (name, color) in cursor]
    cursor.close()
    connection.close()

    return results


def find_data(name) -> List[Dict]:
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    query = 'SELECT * FROM favorite_colors WHERE name=%s'
    val = (name, )
    cursor.execute(query, val)
    results = [{name: color} for (name, color) in cursor]
    cursor.close()
    print('hmmmm')
    connection.close()

    return results


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        if request.form['submitbutton'] == 'Submit':
            name = request.form['fname']
            color = request.form['colorname']
            add_data(name, color)
        elif request.form["submitbutton"] == 'Find':
            name = request.form['kname']
            return redirect(url_for('find', name=name))
        else:
            return json.dumps({'favorite_colors': get_data()})
    return render_template("index.html")


@app.route('/find', methods=["POST", "GET"])
def find(name):
    return json.dumps({'favorite_color': find_data(name)})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
