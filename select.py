import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")


class Select:
    def select_table(self):
        pass