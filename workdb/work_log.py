#!/usr/bin/env python3

from collections import OrderedDict

from peewee import *

db = SqliteDatabase('tasks.db')

class Task(Model):
    username = CharField()
    taskname = CharField()
    duration = IntegerField(default=0)
    notes = TextField()

    class Meta:
        database = db

def initialize():
    """Create the database and table if they don't exist."""
    db.connect()
    db.create_tables([Task], safe=True)

def menu_loop():
    """Show the menu"""
    choice = None
    while choice != 'q':
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print("{}) {}".format(key, value.__doc__))
        choice = input('Action: ').lower().strip()

    if choice in menu:
        menu[choice]()

# As a user of the script,

#  I should be able to choose whether to add a new entry or lookup previous entries.

#  if I choose to enter a new work log, I should be able to provide my name, a task name, a number of minutes spent working on it, and any additional notes I want to record.

#  if I choose to find a previous entry, I should be presented with four options: find by employee, find by date, find by time spent, find by search term.

#  if finding by employee, I should be presented with a list of employees with entries and be able to choose one to see entries from.

#  if finding by employee, I should be allowed to enter employee name and then be presented with entries with that employee as their creator.

#  if finding by date, I should be presented with a list of dates with entries and be able to choose one to see entries from.

#  if finding by time spent, I should be allowed to enter the amount of time spent on the project and then be presented with entries containing that amount of time spent.

#  if finding by a search term, I should be allowed to enter a string and then be presented with entries containing that string in the task name or notes.

# As a fellow developer, I should find at least 50% of the code covered by tests. I would use coverage.py to validate this amount of coverage.
def add_entry():
    pass

def view_entries():
    pass

menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
])

if __name__ == '__main__':
    initialize()
    menu_loop()

