from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import User

# You are importing this base from models file
from models import Base


# Setting up the database connection
engine = create_engine('sqlite:///tatenda.db', echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# ===================== Create the database tables if they do not exist
def create_base():
    Base.metadata.create_all(bind=engine)

# ===================== Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_user(username, password, email):
    with SessionLocal() as db:
        new_user = User(
            username=username,
            password=password,
            email = email
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return f"{new_user.name} account created!!\nUri mhata verenga 🤣"