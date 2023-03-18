from flask import Flask
from database import db_session

from database.users import User
from database.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'nRLhAQWy'


if __name__ == '__main__':
    db_session.global_init('db/mars_explorer.db')
    db_sess = db_session.create_session()

    job = Jobs(team_leader=1, job='deployment of residential modules 1 and 2',
               work_size=15, collaborators='2, 3', is_finished=False)
    db_sess.add(job)
    db_sess.commit()

    # app.run(port=8080, host='127.0.0.1')
