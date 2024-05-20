import unittest
import sqlite3
import os

class TestDatabaseOperations(unittest.TestCase):
    def setUp(self):
        # Create a temporary database for testing
        self.db_file = 'test_example.db'
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, password TEXT, email TEXT)''')
        cursor.execute("INSERT INTO users (name, password, email) VALUES (?, ?, ?)", ('user1', 'pass1', 'user1@example.com'))
        cursor.execute("INSERT INTO users (name, password, email) VALUES (?, ?, ?)", ('user2', 'pass2', 'user2@example.com'))
        conn.commit()
        conn.close()

    def tearDown(self):
        os.remove(self.db_file)

    def test_fetch_data_from_database(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0], (1, 'user1', 'pass1', 'user1@example.com'))
        self.assertEqual(rows[1], (2, 'user2', 'pass2', 'user2@example.com'))
        conn.close()

if __name__ == '__main__':
    unittest.main()
