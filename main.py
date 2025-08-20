from models import UserCreate, User
from sqlalchemy.orm import Session
from controller import create_user, create_base

# This is your guy who is going to create your table in your database
#  Check controller.py Line 15
create_base()


# Example 1 : User creation
# create_user is defined in controller.py Line 26
print(create_user(username="tchitanda", password='12345', email="tchitanda@gmail.com"))