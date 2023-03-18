from flask import Flask
from flask import render_template, render_template_string
from database.db_session import global_init, create_session

from database.users import User
from database.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'nRLhAQWy'


@app.route('/')
def index():
    tables = []
    for job in db_sess.query(Jobs).all():
        team_leader = db_sess.query(User).filter(User.id == job.team_leader).first()
        team_leader = team_leader.surname + team_leader.name
        table = f"""<h3>Action #{job.id}</h3>
    <table border="1">
        <tr>
            <td>Title of activity</td>
            <td>Team leader</td>
            <td>Duration</td>
            <td>List of collaborators</td>
            <td>Is finished</td>
        </tr>
        <tr>
            <td>{job.job}</td>
            <td>{team_leader}</td>
            <td>{job.work_size} hours</td>
            <td>{job.collaborators}</td>
            <td>{'Is finished' if Jobs.is_finished == '1' else 'Is not finished'}</td>
        </tr>
    </table>"""
        tables.append(table)
    return render_template('index.html', tables=tables)


if __name__ == '__main__':
    global_init('db/mars_explorer.db')
    db_sess = create_session()
    app.run(port=5000, host='127.0.0.1')
