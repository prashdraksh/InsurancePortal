from flask import Flask,render_template
import sqlite3

app= Flask(__name__)

@app.route('/')
def log():
    connect=sqlite3.connect('p1dr.db')
    connect.close()
app.run()