import click, pytest, sys
from flask.cli import with_appcontext, AppGroup
import datetime

from App.database import db, get_migrate
from App.models import User, Report
from App.main import create_app
from App.controllers.initialize import initialize
from App.controllers.user import *



# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
@click.argument("email", default="rob@example.com")
def create_user_command(username, password, email):
    create_user(username, password, email)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

#command : flask user userID clockin
@user_cli.command("clockin", help="Clocks into shift if assigned to user")
@click.argument("userID")
def user_clockin_command(userID):
    current_datetime = datetime.now()
    assignmentID = clock_in(userID, current_datetime)
    if assignmentID != None: #uses current system time to clock user in
        print(f'{username} clocked in at {current_datetime.strftime("%I:%M %p")}')
        db.session.add(Report(assignmentID, current_datetime))
        db.session.commit()
    else:
        print('No assigned shift at this time. Please check roster of all available shifts (hint: flask check_roster)')

#command : flask user userID clockout
@user_cli.command("clockout", help="Clocks out of shift for user")
@click.argument("userID")
def user_clockin_command(userID):
    current_datetime = datetime.now()
    assignmentID = clock_out(userID, current_datetime)
    if assignmentID != None: #uses current system time to clock user in
        print(f'{username} clocked out at {current_datetime.strftime("%I:%M %p")}')
        db.session.add(Report(assignmentID, current_datetime))
        db.session.commit()
    else:
        print('User is not working a shift. (hint: flask check_roster)')

app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)