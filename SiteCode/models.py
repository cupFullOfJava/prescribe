from peewee import *


DB_DATA = open('DB_DATA', 'r')
DB_USER = DB_DATA.readline().rstrip()
DB_PASS = DB_DATA.readline().rstrip()

database = MySQLDatabase('prescribe', **{'password': DB_PASS, 'user': DB_USER})


class UnknownField(object):
    pass


class BaseModel(Model):
    class Meta:
        database = database


class Users(BaseModel):
    email = CharField(primary_key=True)
    firstname = CharField(null=True)
    lastname = CharField(null=True)
    user_pw = CharField(null=False)

    class Meta:
        db_table = 'users'


class Searches(BaseModel):
    artist = CharField(db_column='artist_id', primary_key=True)
    email = ForeignKeyField(db_column='email', rel_model=Users, to_field='email', unique=True)

    class Meta:
        db_table = 'searches'

