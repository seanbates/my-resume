##file used to manage the resume page

from flask_script import Manager
from resume import app, db, Professor, Course

manager = Manager(app)

@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    gillespie = Professor(name='Jackson Gillespie', department='Accounting & MIS')
    vermeer = Professor(name='Thomas Vermeer', department='Accounting & MIS')
    dragone = Professor(name='Debra Dragone', department='Accounting & MIS')
    hartono = Professor(name='Edward Hartono', department='Accounting & MIS')
    course1 = Course(course_number= 'ACCT207', title='Accounting I')
    course2 = Course(course_number='ACCT208', title='Accounting II')
    course3 = Course(course_number='MISY160', title='Business Computing: Tools and Concepts')
    course4 = Course(course_number='MISY225', title='Introduction to Programming Business Applications')
    db.session.add(gillespie)
    db.session.add(vermeer)
    db.session.add(dragone)
    db.session.add(hartono)
    db.session.add(course1)
    db.session.add(course2)
    db.session.add(course3)
    db.session.add(course4)
    db.session.commit()

if __name__ == '__main__':
    manager.run()
