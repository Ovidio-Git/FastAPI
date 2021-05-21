import datetime
from peewee import *

database_name='test'

# create a mysql object
database = MySQLDatabase(
    database_name,
    user='root',
    password='991121',
    host='localhost'
)

#table representation
class Dogs(Model):
    id =IntegerField(unique=True, null=False)
    name = CharField(max_length=20, null=False)
    picture = CharField(max_length=100)
    is_adopted = BooleanField(default=True)
    created_date = DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        database = database
        tabel_name = 'Dogs'