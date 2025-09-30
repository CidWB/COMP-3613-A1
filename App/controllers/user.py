from App.models import User, Shift, Report
from App.database import db

username = "tom"
password = "bobpass"
email = "bob@e.x"

def create_user(username, password, email):
    newUser = User(username, password, email)
    db.session.add(newUser)
    db.session.commit()
    return newUser


def get_user_by_username(username):
    result = db.session.execute(db.select(User).filter_by(username=username))
    return result.scalar_one_or_none()

def get_user(id):
    return db.session.get(User, id)

def get_all_users():
    return db.session.scalars(db.select(User)).all()

def get_all_users_json():
    users = get_all_users()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        # user is already in the session; no need to re-add
        db.session.commit()
        return True
    return None
    
def clock_in(userID, clockInTime):
    #initialize new report object
    if not user.assignments: #no assigned shifts
        return None
    user = db.query(User).filter(User.userID == userID)
    shiftMatch = db.query(Shift).filter(Shift.startTime <= clockInTime, clockInTime < Shift.endTime).one()
    
    for assignment in user.assignments:
            for shift in assignment.shifts: #this list cannot be null since it is a composition
                    if shift == shiftMatch:
                            return assignment.assignmentID

    return None
    
def clock_out(userID, clockOutTime): 
    user = db.query(User).filter(User.userID == userID)
    reportID = db.query(Report).filter(Report.assignmentID == assignmentID).one()
    for assignment in user.assignments:
        if reportID == assignment.assignmentID:
                return assignment.assignmentID
    
    return None
    
def view_combined_roster():
    #print roster using something like pipy.tabulate
    return