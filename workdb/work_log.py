#!/usr/bin/env python3

from collections import OrderedDict
import sys

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

def add_entry():
    """Enter a new work log."""
    print("Enter your username. Press ctrl+d when finished.")
    data_username = sys.stdin.read().strip()

    print("Enter a name for your task. Press ctrl+d when finished.")
    data_taskname = sys.stdin.read().strip()

    print("Enter the number of minutes spent on task. Press ctrl+d when finished.")
    data_duration = sys.stdin.read().strip()

    print("Enter additional notes. Press ctrl+d when finished.")
    data_notes = sys.stdin.read().strip()

    if (data_username and data_taskname and data_duration):
        if input("Save work log? [Yn] ") != "n":
            Task.create(
                username = data_username,
                taskname = data_taskname,
                duration = data_duration,
                notes    = data_notes
            )
            print("Work log saved successfully!")

def view_entries():
    """View previous entries."""
    print("How would you live to find a previous entry?")
    choice = None
    while choice != 'q':
        print("Enter 'q' to go back to main menu.")
        for key, value in menu_previous_entry.items():
            print("{}) {}".format(key, value.__doc__))
        choice = input('Action: ').lower().strip()

        if choice in menu:
            menu[choice]()

def find_employee():
    """Find previous entry by employee name."""
    pass

def find_date():
    """Find previous entry by create date."""
    pass

def find_duration():
    """Find previous entry by task duration."""
    pass

def find_search():
    """Find previous entry by notes using search term."""
    pass

menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
])

menu_previous_entry = OrderedDict([
    ('e', find_employee),
    ('t', find_date),
    ('d', find_duration),
    ('s', find_search),
])

if __name__ == '__main__':
    initialize()
    menu_loop()
