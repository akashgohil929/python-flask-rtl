#imports
from flask import Flask , render_template,request
import sqlite3

#setup
app = Flask(__name__)

#routes

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == "POST":

        connection = sqlite3.connect("user_data.db")
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']

        # print(name, password)

        query = "SELECT name,password FROM users WHERE name = '"+name+"' and password = '"+password+"'"
        cursor.execute(query)

        results = cursor.fetchall()

        if len(results)==0 :
            print("incorrect")
        else :
            return render_template("home.html")
    return render_template('login.html')


