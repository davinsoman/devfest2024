import os
import psycopg2
from flask import Flask, render_template
from sqlalchemy import create_engine

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)

DATABASEURI = "postgresql://devfest:hack2024@localhost:5432/devfest"
engine = create_engine(DATABASEURI)



@app.route('/')
def home():
    print("Rendering home page")
    return render_template('home.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)