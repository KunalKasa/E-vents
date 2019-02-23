from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
#from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'E/vents123'
app.config['MYSQL_DB'] = 'e/vents'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact_us')
def event():
    return render_template('contact.html')

@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    if request.method =='POST':
        NAME_ORGANISER = request.form['name_of_organizer']
        LOCATION=request.form['location_of_event']
        GENRE=request.form['genre']
        cur = mysql.connection.cursor()
        query="INSERT INTO edata(NAME_ORGANISER,LOCATION,GENRE) VALUES(%s,%s,%s)"
        cur.execute(query,(NAME_ORGANISER,LOCATION,GENRE))
        mysql.connection.commit()
        cur.close()
    return render_template('predict.html')


if __name__ == '__main__':
    app.run(debug=True)