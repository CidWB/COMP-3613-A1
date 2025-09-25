from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Report(db.Model):
    reportID = db.Column(db.Integer, primary_key=True)
    assignmentID = db.Column(db.Integer, db.ForeignKey('Assignment.assignmentID'), nullable=False)
    clockInTime =  db.Column(db.Time, nullable=False)
    clockOutTime =  db.Column(db.Time, nullable=False)

    def __init__(self, assignmentID, clockInTime):
        self.assignmentID = assignmentID
        self.clockInTime = clockInTime

    def get_json(self):
        return{
            'reportID': self.reportID,
            'assignmentID': self.assignmentID,
            'clockInTime': self.clockInTime
            'clockOutTime': self.clockOutTime
        }


