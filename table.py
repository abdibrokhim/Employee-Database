import pandas as pd
import sqlite3

conn = sqlite3.connect('employee.db')
print("Opened database successfully")


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

    def add_table_info(self):
        print("\n:: FILL IN THE TABLE ::")
        print("input 0 to leave blank\n")

        employee_name = str(input("Input employee name: "))
        employee_age = int(input("Input employee age: "))
        employee_address = str(input("Input employee address: "))
        employee_salary = float(input("Input employee salary: "))
        employee_gender = str(input("Input employee gender: "))

        conn.execute("INSERT INTO employee (NAME, AGE, ADDRESS, SALARY, GENDER)\
        VALUES(?, ?, ?, ?, ?)", (employee_name, employee_age, employee_address, employee_salary, employee_gender))

        conn.commit()

        print("\nSUCCESS")

    def show_table(self):
        table = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", conn)
        print("\n", table, "\n")

        print("\nSUCCESS")

    def select_table_info(self):
        data = conn.execute("SELECT id, name, address, salary, gender from employee")

        for row in data:
            print("ID = ", row[0])
            print("NAME = ", row[1])
            print("ADDRESS = ", row[2])
            print("SALARY = ", row[3])
            print("GENDER = ", row[4], "\n")

        print("\nSUCCESS")

    def update_table_info(self):
        pass

    def delete_table(self):
        print("\n:: DELETE TABLE ::")

        table_name = str(input("\nInput table name: "))
        table = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", conn)

        if table_name in str(table):
            conn.execute("DROP TABLE {}".format(table_name))

            print("\nSUCCESS")
        else:
            print("INVALID")
