from peewee import *

database_name='test'

# create a mysql object
database = MySQLDatabase(
    database_name,
    user='root',
    password='991121',
    host='localhost'
)