from peewee import *

db = SqliteDatabase("tasks.db")


class Task(Model):
    username = CharField(max_length=255, unique=False)
    taskname = CharField(max_length=255, unique=False)
    duration = IntegerField(default=0)

    class Meta:
        database = db


if __name__ == '__main__':
    db.connect()
    db.create_tables([Task], safe=True)
