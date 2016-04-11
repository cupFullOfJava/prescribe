from peewee import *

database = MySQLDatabase('prescribe', **{'password': 'prescribeapppass', 'user': 'prescribeapp'})


class UnknownField(object):
    pass


class BaseModel(Model):
    class Meta:
        database = database


class Users(BaseModel):
    user_pw = CharField(null=True)
    username = CharField(primary_key=True)

    class Meta:
        db_table = 'users'


class Searches(BaseModel):
    artist = DecimalField(db_column='artist_id', primary_key=True)
    username = ForeignKeyField(db_column='username', rel_model=Users, to_field='username', unique=True)

    class Meta:
        db_table = 'searches'

