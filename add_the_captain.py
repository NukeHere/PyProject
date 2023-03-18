from flask import Flask
from database import db_session

from database.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'nRLhAQWy'


if __name__ == '__main__':
    db_session.global_init('db/mars_explorer.db')
    db_sess = db_session.create_session()
    captain = User(surname='Scott', name='Ridley', age=21, position='captain',
                   speciality='research engineer', address='module_1', email='scott_chief@mars.org')

    user_0 = User(surname='Petrov', name='Peta', age=22, position='cleaner',
                  speciality='clean master', address='module_2', email='cleaning@mars.org')
    user_1 = User(surname='Ivanov', name='Ivan', age=9, position='engineer',
                  speciality='engineer', address='module_3', email='engineer_ivanov@mars.org')
    user_2 = User(surname='Motrosov', name='Cot', age=-1, position='cooker',
                  speciality='cooker', address='module_0', email='cookers@mars.org')
    db_sess.add(captain)
    db_sess.add(user_0)
    db_sess.add(user_1)
    db_sess.add(user_2)
    db_sess.commit()

    # app.run(port=8080, host='127.0.0.1')
