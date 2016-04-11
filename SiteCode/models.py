"""
These classes describe the database structure and tables that are used to keep track of users
and their saved searches.
"""
from peewee import *

database = MySQLDatabase('presribe', **{'password': 'prescribeapppass', 'user': 'prescribeapp'})


class UnknownField(object):
    pass


# The database that the tables use
class BaseModel(Model):
    class Meta:
        database = database


# The users table
class Users(BaseModel):
    user_pw = CharField(null=True)
    username = CharField(primary_key=True)

    class Meta:
        db_table = 'users'


# The searches table
class Searches(BaseModel):
    artist = DecimalField(db_column='artist_id', primary_key=True)
    username = ForeignKeyField(db_column='username', rel_model=Users, to_field='username', unique=True)

    class Meta:
        db_table = 'searches'

