from backend import Database

class Client(object):
    """Class that contains methods for:
    choosing whether to [A]dd a new entry or [L]ookup previous entries,
    if [A] then provide (name, task name, duration, notes),
    if [L] then find by (employee, date, duration, search term),
    if [L] and find by employee then present list of employees and choose an entry,
    if [L] and find by date then present list of dates and choose an entry,
    if [L] and find by duration then enter a duration and choose an entry with that duration,
    if [L] and find by search term then present a list and choose an entry with that search term."""
    def __init__(self):
        pass

    def run(self):
        """Run the client application until the user exits."""
        input("""Would you like to
        [A]dd an entry
        [L]ookup an entry
        [Q]uit this application? """)
