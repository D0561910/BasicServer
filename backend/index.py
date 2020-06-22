# Learn From 
# https://blog.techbridge.cc/2017/06/03/python-web-flask101-tutorial-introduction-and-environment-setup/
# https://www.maxlist.xyz/2019/11/10/flask-sqlalchemy-setting/
# https://hackersandslackers.com/flask-sqlalchemy-database-models/
# https://stackoverflow.com/questions/9845102/using-mysql-in-flask
# https://stackoverflow.com/questions/25398218/getting-json-response-using-requests-object-flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask import request

db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@127.0.0.1:3306/testDB"

db.init_app(app)

@app.route('/')
def index():

    username = request.args.get('username')
    password = request.args.get('password')

    sql_cmd = """
        select *
        from account
        """

    # Get data from MySQL Database
    query_data = db.engine.execute(sql_cmd)
    
    # Decode query data
    d, a = {}, []
    for rowproxy in query_data:
        # rowproxy.items() returns an array like [(key0, value0), (key1, value1)]
        for column, value in rowproxy.items():
            # build up the dictionary
            d = {**d, **{column: value}}
        a.append(d)
    status = False
    for i in range(len(a)):
        ids = a[i]['PersonID']
        passwords = a[i]['Pass']
        if(ids == username and passwords == password):
            status = True

    if(status):
        return "true"
    else:
        return "false"

@app.route('/create')
def create():

    username = request.args.get('username')
    password = request.args.get('password')

    newAccount = """ INSERT INTO account (PersonID, Pass) VALUES (\"{}\", \"{}\") """.format(username, password)
    # print(newAccount)
    db.engine.execute(newAccount)
    # db.session.add(newAccount)
    # db.session.commit()

    print(username)
    print(password)

    return 'ok create'

if __name__ == "__main__":
    app.run()
