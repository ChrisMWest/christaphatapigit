from sqlalchemy import create_engine, MetaData, Table, sql, and_
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:123@localhost/christaphat_dev")
metadata = MetaData()
user = Table("user_data", metadata, autoload_with = engine)
item = Table("item_data", metadata, autoload_with = engine)
Session = sessionmaker(bind = engine)

def add_user(name, email):
    session = Session()
    s = user.insert(values = dict(name=name, email=email))
    session.execute(s)
    session.commit()
    result = session.execute("select * from user_data")
    print(result.fetchall())

def remove_user(name, email):
    session = Session()
    s = user.delete().where(and_(user.c.name == name, user.c.email == email))
    session.execute(s)
    session.commit()
    result = session.execute("select * from user_data")
    print(result.fetchall())

def add_user_item(user_id, name, genre, description, rank):
    session = Session()
    s = item.insert(values = dict(user_id=user_id, name=name, genre=genre, description=description, rank=rank))
    session.execute(s)
    session.commit()
    result = session.execute("select * from item_data")
    print(result.fetchall())

def remove_user_item(user_id, name, genre, description, rank):
    session = Session()
    s = item.delete().where(and_(item.c.user_id == user_id, item.c.name == name, item.c.genre == genre, item.c.description == description, item.c.rank == rank))
    session.execute(s)
    session.commit()
    result = session.execute("select * from item_data")
    print(result.fetchall())

#def display_user_items(user_id):

add_user("vernon", "vliu@uvic.ca")
remove_user("anu", "asinhae")
add_user_item(2, "clannad", "anime", "love story", 1)
add_user_item(5, "boku no pico", "anime", "weird hentai shit", 1)
remove_user_item(7, "boku no pico", "anime", "weird hentai shit", 1)