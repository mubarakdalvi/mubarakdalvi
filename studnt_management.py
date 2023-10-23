from flask import Flask,request
import sqlite3

app = Flask(__name__)


connection = sqlite3.connect('sms.db')
curser = connection.cursor()
curser.execute('create table if not exists students (sid integer primary key,name text,age integer,address text)')
connection.close()

@app.route('/student_details')
def details():
    connection = sqlite3.connect('sms.db')
    curser = connection.cursor()
    return {'students' : list(curser.execute('select * from students'))}

@app.route('/details',methods = ['POST'])
def register():
    data = request.get_json()
    connection = sqlite3.connect('sms.db')
    curser = connection.cursor()
    curser.execute("insert into students values('{},{},{},{}')".format(data['sid'],data['name'],data['age'],data['address']))
    connection.commit()
    connection.close()
    return 'User Created Successfully.. '
app.run(port=5000)