from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Staff(User):
    def __init__(self, username, password): #idk if i need this
        self.username = username
        self.set_password(password) 

    def view_combined_roster():
        #print roster using something like pipy.tabulate
    
    def clock_in(self, assignmentID, clockInTime):
        #initialize new report object
    
    def clock_out(self, assignmentID, clockOutTime): 
        self.clockOutTime = clockOutTime