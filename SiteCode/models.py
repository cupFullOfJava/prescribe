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
    email = CharField(unique=True)
    firstname = CharField(null=True)
    lastname = CharField(null=True)
    user_pw = CharField(null=True)

    class Meta:
        db_table = 'users'


class Searches(BaseModel):
    artist = CharField(db_column='artist_id')
    user = ForeignKeyField(db_column='user_id', rel_model=Users, to_field='id')

    class Meta:
        db_table = 'searches'
        indexes = (
            (('user', 'artist'), True),
        )
        primary_key = CompositeKey('artist', 'user')
