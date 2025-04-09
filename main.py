from sqlalchemy import Column, Integer, String, create_engine, Sequence, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine("sqlite:///example.db", echo=True)

SessionMaker = sessionmaker(bind=engine)
session = SessionMaker()
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    email = Column(String)


Base.metadata.create_all(engine) #Create the tables in the database

user1 = User(name='monir', email='monir@gmail.com')
user2 = User(name='mon', email='moni@gmail.com')

#these two lines are used to add the users to the database
# session.add_all([user1, user2])
# session.commit()

#now we will query the database to get the users
user = session.query(User).filter_by(name='mon').first()
# for user in user:
if user:
    print(user.name, user.email)
else:
    print("User not found")
# print(user.name, user.email)


#now we will delete the users from the database
# session.delete(user)
# session.commit()