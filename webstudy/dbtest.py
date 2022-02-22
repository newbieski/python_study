import mysql.connector
from flask import Flask
from flask import g
from flask import render_template
from flask import request
from flask import Response

app = Flask(__name__)

def get_db():
    db = mysql.connector.connect(host='', user='', password='', database='test_mysql_database')
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = get_db()
    db.close()

@app.route('/employee', methods=['POST', 'PUT', 'DELETE'])
@app.route('/employee/<name>', methods=['GET'])
def employee(name=None) :
    db = get_db()
    curs = db.cursor()
    curs.execute (
        'CREATE TABLE IF NOT EXISTS persons('
        'id int NOT NULL AUTO_INCREMENT, '
        'name varchar(14) NOT NULL,'
        'PRIMARY KEY(id))')
    name = request.values.get('name', name)
    if request.method == 'GET':
        curs.execute('SELECT * FROM persons WHERE name = "{}"'.format(name))
        person = curs.fetchone()
        if not person:
            return "No", 404
        user_id, name = person
        return '{}:{}'.format(user_id, name), 200
    if request.method == 'POST':
        curs.execute('INSERT INTO persons(name) values("{}")'.format(name))
        db.commit()
        return 'created {}'.format(name), 201
    if request.method == 'PUT':
        new_name = request.values['new_name']
        curs.execute('UPDATE persons set name = "{}" WHERE name = "{}"'.format(new_name, name))
        db.commit()
        return 'updated {}: {}'.format(name, new_name), 200
    if request.method == 'DELETE':
        curs.execute('DELETE from persons WHERE name = "{}"'.format(name))
        db.commit()
        return 'deleted {}'.format(name), 200


@app.route('/')
def hello_world():
    return render_template('fillform.html')

@app.route('/hello/')
@app.route('/hello/<username>')
def hello_world2(username=None) :
    #return 'hello world! {}'.format(username)
    return render_template('hello.html', username=username)

@app.route('/post', methods=['POST', 'PUT', 'DELETE'])
def show_post():
    return str(request.values)

def main():
    app.debug = True
    app.run(host='127.0.0.1', port='5001')

if __name__ == '__main__' :
    main()