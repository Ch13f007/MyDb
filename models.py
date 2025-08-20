from sqlalchemy import Column, Boolean, String, Integer,DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from pydantic import BaseModel, validator
from datetime import datetime,timedelta 


# Base Instance for models
Base = declarative_base()

# =================================User template (login via user name and password)
# This is the user model that will be used to create the user table in the database
# It contains the user information such as username, password and created_at
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    password = Column(String(50))
    email = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)

# =================================Pydantic template for user creation
# This is used to validate the data when creating a new user
# It contains the user information such as username, and password
# The password will be hashed before storing it in the database 
class UserCreate(BaseModel):
    username: str
    password: str
    email: str = ""