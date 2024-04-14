"""
@author: NTK
"""
import sys

from sqlalchemy import create_engine, String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
db = "mysql+mysqldb://root:root@localhost:3306/hbtn_0e_0_usa" #connection string to describe mysql database
engine = create_engine(db) # creates an engine object to establish connection with Mysql database
Base.metadata.create_all(engine) # creates a table in Mysql database (if it doesn't already exist)
Session = sessionmaker(bind=engine) # creates session object which interacts with the database
session = Session()


class states(Base):
    __tablename__="states"
    id = Column("id", Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column("firstName", String(254))

    def __init__(self, id, name):
        self.id = id
        self.name= name

if __name__ == '__main__':
    if len(sys.argv == 3):
      allStates= session.query(states).all()
      S = [(s.id, s.name) for s in allStates]
      print(S)
    else:
        pass