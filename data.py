import pandas as pd
import sqlite3

conn = sqlite3.connect('employee.db')


class Data:
    def __init__(self):
        pass

    def add_table_data(self):
        print("\n:: FILL IN THE TABLE DATA::")
        print("input 0 to leave blank\n")
        table_name = str(input("Input table name: "))
        employee_name = str(input("Input employee name: "))
        employee_age = int(input("Input employee age: "))
        employee_address = str(input("Input employee address: "))
        employee_salary = float(input("Input employee salary: "))
        employee_gender = str(input("Input employee gender: "))

        conn.execute('INSERT INTO {} (NAME, AGE, ADDRESS, SALARY, GENDER)\
        VALUES(?, ?, ?, ?, ?)'.format(table_name), (employee_name, employee_age, employee_address, employee_salary, employee_gender))

        conn.commit()

        print("\nSUCCESS")

    def show_table_data(self):
        print("\n:: SHOW THE TABLE DATA ::")
        table_name = str(input("\nInput table name: "))
        table = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", conn)
        if table_name in str(table):
            data = conn.execute("SELECT * from {}".format(table_name))
            for row in data:
                print("ID: ", row[0])
                print("NAME: ", row[1])
                print("AGE: ", row[2])
                print("ADDRESS: ", row[3])
                print("SALARY: ", row[4])
                print("GENDER: ", row[5], "\n")

            print("\nSUCCESS")
        else:
            print("\nINVALID")

    def update_table_data(self):
        print("\n:: UPDATE THE TABLE DATA ::")
        print("input 0 to leave unchanged\n")
        table_name = str(input("\nInput table name: "))

        self.update_table_data_set(table_name)

    def update_table_data_set(self, table_name):
        while True:
            print("\n:: CHOOSE AN OPTION ::\n")
            print("[1] -> UPDATE NAME")
            print("[2] -> UPDATE AGE")
            print("[3] -> UPDATE ADDRESS")
            print("[4] -> UPDATE SALARY")
            print("[5] -> UPDATE GENDER")
            print("[6] -> EXIT\n")

            choice = input("[?] -> ")

            try:
                choice = int(choice)
            except ValueError:
                print("\nINVALID")
                continue

            if choice == 1:
                employee_name = str(input("Update employee name: "))
                Data.update_table_data_where(self, table_name, employee_name)
            elif choice == 2:
                employee_age = int(input("Update employee age: "))
                Data.update_table_data_where(self, table_name, employee_age)
            elif choice == 3:
                employee_address = str(input("Update employee address: "))
                Data.update_table_data_where(self, employee_address, employee_address)
            elif choice == 4:
                employee_salary = float(input("Update employee salary: "))
                Data.update_table_data_where(self, employee_salary, employee_salary)
            elif choice == 5:
                employee_gender = str(input("Update employee gender: "))
                Data.update_table_data_where(self, employee_gender, employee_gender)
            elif choice == 6:
                exit()
            else:
                print("\nINVALID")

    def update_table_data_where(self, table, arg):
        while True:
            print("\n:: CHOOSE AN OPTION ::\n")
            print("[1] -> WHERE NAME")
            print("[2] -> WHERE AGE")
            print("[3] -> WHERE ADDRESS")
            print("[4] -> WHERE SALARY")
            print("[5] -> WHERE GENDER")
            print("[6] -> EXIT\n")

            choice = input("[?] -> ")

            try:
                choice = int(choice)
            except ValueError:
                print("\nINVALID")
                continue

            if choice == 1:
                employee_name = str(input("where employee name: "))
                conn.execute('UPDATE {} SET {} WHERE NAME = {}'.format(table, arg, employee_name))

                conn.commit()

                print("\nSUCCESS")

            elif choice == 2:
                employee_age = int(input("where employee age: "))
            elif choice == 3:
                employee_address = str(input("where employee address: "))
            elif choice == 4:
                employee_salary = float(input("where employee salary: "))
            elif choice == 5:
                employee_gender = str(input("where employee gender: "))
            elif choice == 6:
                exit()
            else:
                print("\nINVALID")

    def delete_table_data(self):
        print("\nin development")

    def select_table_data(self):
        print("\nin development")