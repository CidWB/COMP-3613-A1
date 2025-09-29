from werkzeug.security import generate_password_hash
from App.database import db
from App.models.User import *


username = "bob"
password = "bobpass"
email = "bob@e.x"
newUser = User(username, password, email)
db.session.add(newUser)


def print_password(password):
        """Create hashed password."""
        print (f"This is bob's password: {password}")
        password = generate_password_hash(password)
        print (f"This is bob's hashed password: {password}")

print_password(password)
print("hello world!")