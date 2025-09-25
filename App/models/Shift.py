from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Shift(db.Model):
    shiftID = db.Column(db.Integer, primary_key=True)
    date =  db.Column(db.Date, nullable=False)
    startTime =  db.Column(db.Time, nullable=False)
    endTime =  db.Column(db.Time, nullable=False)

    def __init__(self, date, startTime, endTime):
        self.date = date
        self.startTime = startTime
        self.endTime = endTime

    def get_json(self):
        return{
            'shiftID': self.shiftID,
            'date': self.date
            'startTime': self.startTime
            'endTime': self.endTime
        }

