from flask import Blueprint, render_template, request, redirect
from flask_mysqldb import MySQL

main = Blueprint('main', __name__)

mysql = MySQL()

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)", (name, email))
        mysql.connection.commit()
        cur.close()

        return redirect('/')
    return render_template('index.html')
