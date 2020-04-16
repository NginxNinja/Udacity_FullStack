# Initialize the engin
import os
from sqlalchemy import create_engine, Column, String, Integer

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

database_filename = 'playground.db'
# project_dir = os.path.dirname(os.path.abspath(''))
project_dir = os.path.dirname(os.path.relpath('/'))
database_path = 'sqlite:///{}'.format(os.path.join(project_dir, database_filename))

engine = create_engine(database_path)

# Define a model class
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    # Autoincrementing, primary key
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    # String Title
    username = Column(String(80), unique=True)
    password = Column(String(180), nullable=False)

    def __repr__(self):
        return self.username +": "+self.password

User.metadata.create_all(engine)

User.__tablename__

# Initialize a session
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()

# Add a new user
session.rollback()

new_user = User(username='James', password='superstrongpassword')
session.add(new_user)
session.commit()

# Fetch a user from the database
db_user = session.query(User).filter_by(username='James').first()
print(db_user)

# > TIP: If you get stuck with errors, try executing this block:
session.rollback()