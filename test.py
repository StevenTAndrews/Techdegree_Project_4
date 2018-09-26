import unittest
import os
from unittest.mock import patch

import worklog_database


class WorklogTests(unittest.TestCase):
    def setUp(self):
        self.name = 'Name'
        self.task = 'Test'
        self.time = 5
        self.notes = 'Notes'
        worklog_database.Entry.create(name=self.name,
            task=self.task,
            time=self.time,
            notes=self.notes)

    def test_db_initialize(self):
        worklog_database.initialize()
        self.assertTrue(os.path.isfile('work_log.db'))



    def test_add_entry(self):
        self.assertEqual(worklog_database.Entry.name, self.name)
        self.assertEqual(worklog_database.Entry.task, self.task)
        self.assertEqual(worklog_database.Entry.time, self.time)
        self.assertEqual(worklog_database.Entry.notes, self.notes)



    def test_name_search(self):
        """Make sure the Name search finds Name."""
        with unittest.mock.patch('builtins.input', return_value='Name'):
            self.assertFalse(worklog_database.name_search() != None)


    def test_task_search(self):
        """Make sure the Task search finds Task."""
        with unittest.mock.patch('builtins.input', return_value='Test'):
            self.assertFalse(worklog_database.task_search('Test') != None)


    def test_note_search(self):
        """Make sure the Note search finds Notes."""
        with unittest.mock.patch('builtins.input', return_value='Notes'):
            self.assertFalse(worklog_database.note_search() != None)
        
            






if __name__ == '__main__':
    unittest.main()