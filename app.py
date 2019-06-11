from flask import Flask, render_template, request
import sqlite3


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def posting_the_post():
    conn = sqlite3.connect('blogs.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE bloggers (first text, last text, post text)""")

    saxeli = request.form['saxeli']
    gvari = request.form['gvari']
    posti = request.form['posti']
    params = (saxeli, gvari, posti)
    c.execute(f"INSERT INTO bloggers VALUES (?, ?, ?)", params)
    conn.commit()
    conn.close()
    return 'All caught up!'


app.run()
