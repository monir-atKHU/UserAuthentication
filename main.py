from sqlalchemy import Column, Integer, String, create_engine, Sequence, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# engine = create_engine("sqlite:///example.db", echo=True)
engine = create_engine("sqlite:///example.db")

SessionMaker = sessionmaker(bind=engine)
session = SessionMaker()
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    email = Column(String)
    posts = relationship("Post", back_populates="user")


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, Sequence('post_id_seq'), primary_key=True)
    title = Column(String(50))
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="posts")


Base.metadata.create_all(engine) #Create the tables in the database

user1 = User(name='monir', email='monir@gmail.com')
user2 = User(name='mon', email='moni@gmail.com')


post1 = Post(title='monirs 1', content = 'fisrst content', user = user1)
post2 = Post(title='mons 1', content = 'second content', user = user2)
post3 = Post(title='monirs 2', content = 'third content', user = user1)

#these two lines are used to add the users to the database
session.add_all([user1, user2, post1, post2, post3])
session.commit()

posts_with_users = session.query(Post).join(User).all()

for post in posts_with_users:
    print(f"Post Title: {post.title}, User Name: {post.user.name}")





#now we will query the database to get the users
# user = session.query(User).filter_by(name='mon').first()
# # for user in user:
# if user:
#     print(user.name, user.email)

# else:
#     print("User not found")
# # print(user.name, user.email)


# #now we will delete the users from the database
# # session.delete(user)
# # session.commit()  