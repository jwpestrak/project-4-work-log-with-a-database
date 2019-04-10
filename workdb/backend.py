from peewee import *

db = SqliteDatabase("tasks.db")


class Task(Model):
    username = CharField(max_length=255, unique=False)
    taskname = CharField(max_length=255, unique=False)
    duration = IntegerField(default=0)

    class Meta:
        database = db


tasks = [
    {'username': 'James',
     'taskname': 'wake up',
     'duration': 10},
    {'username': 'Georgia',
     'taskname': 'eat breakfast',
     'duration': 5},
]


def add_tasks():
    for task in tasks:
        try:
            Task.create(username=task['username'],
                        taskname=task['taskname'],
                        duration=task['duration'])
        except IntegrityError:
            task_record = Task.get(username=task['username'])
            task_record.duration = task['duration']
            task_record.save()


if __name__ == '__main__':
    db.connect()
    db.create_tables([Task], safe=True)
    add_tasks()
