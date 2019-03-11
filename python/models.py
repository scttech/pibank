from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+mysqlconnector://root:pibank@localhost/pibank',echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
    autoflush=False,
    bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    ssn = Column(Integer)
    job = Column(String)
    age = Column(Integer)
