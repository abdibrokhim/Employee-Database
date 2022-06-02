from data import Data

import pandas as pd
import sqlite3

conn = sqlite3.connect('employee.db')
print("DATABASE OPENED")


class Table:

    def __init__(self):
        pass

    def create_table(self):
        print("\n:: NEW TABLE ::")
        table_name = str(input("\nInput table name: "))

        conn.execute('''CREATE TABLE {}
                 (ID            INTEGER PRIMARY KEY AUTOINCREMENT,
                 NAME           CHAR(50)            NOT NULL,
                 AGE            INT                 NOT NULL,
                 ADDRESS        CHAR(50),
                 SALARY         REAL,
                 GENDER         CHAR(10));'''.format(table_name))

        print("\nSUCCESS")

    def show_table(self):
        table = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", conn)
        print("\n", table, "\n")

        print("\nSUCCESS")

    def delete_table(self):
        print("\n:: DELETE TABLE ::")

        table_name = str(input("\nInput table name: "))
        table = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", conn)

        if table_name in str(table):
            conn.execute("DROP TABLE {}".format(table_name))

            print("\nSUCCESS")
        else:
            print("INVALID")

    def show_more(self):
        data = Data()

        while True:
            print("\n:: CHOOSE AN OPTION ::\n")
            print("[1] -> UPDATE TABLE DATA")
            print("[2] -> DELETE TABLE DATA")
            print("[3] -> ADD TABLE DATA")
            print("[4] -> SELECT TABLE DATA")
            print("[5] -> SHOW TABLE DATA")
            print("[6] -> EXIT\n")

            choice = input("[?] -> ")

            try:
                choice = int(choice)
            except ValueError:
                print("\nINVALID")
                continue

            if choice == 1:
                data.update_table_data()
            elif choice == 2:
                data.delete_table_data()
            elif choice == 3:
                data.add_table_data()
            elif choice == 4:
                data.select_table_data()
            elif choice == 5:
                data.show_table_data()
            elif choice == 6:
                exit()
            else:
                print("\nINVALID")