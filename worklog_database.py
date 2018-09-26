from collections import OrderedDict
import datetime
import os
import sys

from peewee import *

db = SqliteDatabase('work_log.db')


class Entry(Model):
    name = CharField()
    task = CharField()
    time = IntegerField(default=0)
    notes = TextField(default='')
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


def initialize():
    """Create database and table if they don't exist."""
    db.connect(reuse_if_open=True)
    db.create_tables([Entry], safe=True)


def clear():
    """Clear the screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def menu_loop():
    """Show the menu."""
    choice = None

    while choice != 'q':
        clear()
        print('Work Log')
        print('='*8)
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        print('q) Quit.')
        choice = input('Action:  ').lower().strip()

        if choice in menu:
            clear()
            menu[choice]()


def search_menu():
    """Search for an entry."""
    search_choice = None

    while search_choice != 'q':
        clear()
        print('Search Options')
        print('='*14)
        for key, value in search_menu.items():
            print('{}) {}'.format(key, value.__doc__))
        print('q) Back to menu.')
        search_choice = input('Action:   ').lower().strip()

        if search_choice in search_menu:
            clear()
            search_menu[search_choice]()


def add_entry():
    """Add an entry."""
    employee_name = input('Enter your name:   ')
    emplyee_task = input('Task:   ')
    time_took = input('Duration:   ')
    any_notes = input('Notes:   ')
    Entry.create(name=employee_name,
        task=emplyee_task,
        time=time_took,
        notes=any_notes)
    print('Entry saved!')


def name_search():
    """Search entries by name."""
    the_name = input('What name do you want to search?    ')
    entries = Entry.select().order_by(Entry.timestamp.desc())
    entries = entries.where(Entry.name.contains(the_name))
    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        clear()
        print(timestamp)
        print('='*len(timestamp))
        print('Name: {}'.format(entry.name))
        print('Task: {}'.format(entry.task))
        print('Time Spent: {}'.format(entry.time))
        print('Notes: {}'.format(entry.notes))
        print('\n\n'+'='*len(timestamp))
        print('n) next entry.')
        print('q) return to main menu.')

        next_action = input('Action: [Nq]  ').lower().strip()
        if next_action == 'q':
            break


def date_search():
    """Search entries by date."""
    the_date = input('What date do you want to search?  YYYY-MM-DD  ')
    entries = Entry.select().order_by(Entry.timestamp.desc())
    entries = entries.where(Entry.timestamp.contains(the_date))
    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        clear()
        print(timestamp)
        print('='*len(timestamp))
        print('Name: {}'.format(entry.name))
        print('Task: {}'.format(entry.task))
        print('Time Spent: {}'.format(entry.time))
        print('Notes: {}'.format(entry.notes))
        print('\n\n'+'='*len(timestamp))
        print('n) Next entry.')
        print('q) Return to main menu.')

        next_action = input('Action: [Nq]  ').lower().strip()
        if next_action == 'q':
            break


def time_search():
    """Search by amount of time taken."""
    the_time = input('What time ammount would you like to search?  ')
    entries = Entry.select().order_by(Entry.timestamp.desc())
    entries = entries.where(Entry.time==the_time)
    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        clear()
        print(timestamp)
        print('='*len(timestamp))
        print('Name: {}'.format(entry.name))
        print('Task: {}'.format(entry.task))
        print('Time Spent: {}'.format(entry.time))
        print('Notes: {}'.format(entry.notes))
        print('\n\n'+'='*len(timestamp))
        print('n) Next entry.')
        print('q) Return to main menu.')

        next_action = input('Action: [Nq]  ').lower().strip()
        if next_action == 'q':
            break


def note_search():
    """Search by keyword."""
    keyword = input('What word would you like to search by?    ')
    entries = Entry.select().order_by(Entry.timestamp.desc())
    entries = entries.where(Entry.notes.contains(keyword))
    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        clear()
        print(timestamp)
        print('='*len(timestamp))
        print('Name: {}'.format(entry.name))
        print('Task: {}'.format(entry.task))
        print('Time Spent: {}'.format(entry.time))
        print('Notes: {}'.format(entry.notes))
        print('\n\n'+'='*len(timestamp))
        print('n) Next entry.')
        print('q) Return to menu.')

        next_action = input('Action:   [Nq]  ').lower().strip()
        if next_action == 'q':
            break
    task_search(keyword)

def task_search(keyword):
    keyword = keyword
    entries = Entry.select().order_by(Entry.timestamp.desc())
    entries = entries.where(Entry.task.contains(keyword))
    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        clear()
        print(timestamp)
        print('='*len(timestamp))
        print('Name: {}'.format(entry.name))
        print('Task: {}'.format(entry.task))
        print('Time Spent: {}'.format(entry.time))
        print('Notes: {}'.format(entry.notes))
        print('\n\n'+'='*len(timestamp))
        print('n) Next entry.')
        print('q) Return to menu.')

        next_action = input('Action:   [Nq]  ').lower().strip()
        if next_action == 'q':
            break


menu = OrderedDict([
     ('a', add_entry),
     ('s', search_menu),
])   


search_menu = OrderedDict([
    ('n', name_search),
    ('d', date_search),
    ('t', time_search),
    ('w', note_search),
])

if __name__ == '__main__':
    initialize()
    menu_loop()