from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.config import DATABASE_URL


def main():
    engine = create_engine(DATABASE_URL)
    session = Session(binds=engine.connect())
    session.execute(""" create table users (
    id = integer not null primary key, 
    email = varchar(255),
    password = varchar(255),
    first_name = varchar(255),
    last_name = varchar(255),
    nikname = varchar(255),
    created_at = varchar(255),
    position = varchar(255),
    last_login = varchar(255)
    );""")

    session.execute(""" create table auth_token (
        id = integer not null primary key, 
        email = varchar(255),
        token = varchar(255),
        user_id = integer, reference users,
        created_at = varchar(255)
        );""")

    session.execute(""" create table stream (
    id = integer not null primary key,
    user_id = integer, reference users,
    title = varchar(255),
    topic = varchar(255),
    status = varchar(255),
    created_at = varchar(255)
    );""")


if __name__ == '__main__':
    main()
