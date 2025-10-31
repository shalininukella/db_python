from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///practice.db", echo=False)
# echo=True → logs all SQL statements

sessionLocal = sessionmaker(bind=engine)
session = sessionLocal()

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

    # def __repr__(self):
    #     return f"<User(name={self.name}, age={self.email})>"

Base.metadata.create_all(engine)
