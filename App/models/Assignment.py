from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
import datetime

class Assignment(db.Model):
    assignmentID = db.Column(db.Integer, primary_key=True)
    staffID = db.Column(db.Integer, db.ForeignKey('Staff.staffID'), nullable=False)
    shiftID = db.Column(db.Integer, db.ForeignKey('Shift.shiftID'), nullable=False)

    def __init__(self, staffID, shiftID):
        self.staffID = staffID
        self.shiftID = shiftID

    def get_json(self):
        return{
            'assignmentID': self.assignmentID,
            'staffID' : self.staffID,
            'shiftID' : self.shiftID
        }
    
    @staticmethod
    def checkAssignment(staffID, ):
        pass

