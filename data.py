import pandas as pd
import sqlite3

conn = sqlite3.connect('employee.db')


class Data:
    def __init__(self):
        pass

    def add_table_data(self):
        print("\n:: FILL IN THE TABLE DATA::")
        print("input null to leave blank\n")

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
        table_name = str(input("\nInput table name: "))

        Data.update_table_data_set(self, table_name)

    def update_table_data_set(self, table_name):
        while True:
            print("\n:: CHOOSE AN OPTION ::\n")
            print("[1] -> UPDATE NAME")
            print("[2] -> UPDATE AGE")
            print("[3] -> UPDATE ADDRESS")
            print("[4] -> UPDATE SALARY")
            print("[5] -> UPDATE GENDER")
            print("[6] -> BACK\n")

            choice = input("[?] -> ")

            try:
                choice = int(choice)
            except ValueError:
                print("\nINVALID")
                continue

            if choice == 1:
                employee_name = str(input("Update employee name: "))
                name = "NAME"
                Data.update_table_data_where(self, table_name, name, employee_name)

            elif choice == 2:
                employee_age = int(input("Update employee age: "))
                age = "AGE"
                Data.update_table_data_where(self, table_name, age, employee_age)

            elif choice == 3:
                employee_address = str(input("Update employee address: "))
                address = "ADDRESS"
                Data.update_table_data_where(self, table_name, address, employee_address)

            elif choice == 4:
                employee_salary = float(input("Update employee salary: "))
                salary = "SALARY"
                Data.update_table_data_where(self, table_name, salary, employee_salary)

            elif choice == 5:
                employee_gender = str(input("Update employee gender: "))
                gender = "GENDER"
                Data.update_table_data_where(self, table_name, gender, employee_gender)

            elif choice == 6:
                # exit()
                return False
            else:
                print("\nINVALID")

    def update_table_data_where(self, table, arg, kwarg):
        while True:
            print("\n:: CHOOSE AN OPTION ::\n")
            print("[1] -> WHERE NAME")
            print("[2] -> WHERE AGE")
            print("[3] -> WHERE ADDRESS")
            print("[4] -> WHERE SALARY")
            print("[5] -> WHERE GENDER")
            print("[6] -> BACK\n")

            choice = input("[?] -> ")

            try:
                choice = int(choice)
            except ValueError:
                print("\nINVALID")
                continue

            if choice == 1:
                employee_name = str(input("where employee name: "))
                conn.execute('UPDATE {} SET {} = ? WHERE NAME = ?'.format(table, arg), (kwarg, employee_name))
                conn.commit()
                print("\nSUCCESS")
                return False

            elif choice == 2:
                employee_age = int(input("where employee age: "))
                conn.execute('UPDATE {} SET {} = ? WHERE AGE = ?'.format(table, arg), (kwarg, employee_age))
                conn.commit()
                print("\nSUCCESS")
                return False

            elif choice == 3:
                employee_address = str(input("where employee address: "))
                conn.execute('UPDATE {} SET {} = ? WHERE ADDRESS = ?'.format(table, arg), (kwarg, employee_address))
                conn.commit()
                print("\nSUCCESS")
                return False

            elif choice == 4:
                employee_salary = float(input("where employee salary: "))
                conn.execute('UPDATE {} SET {} = ? WHERE SALARY = ?'.format(table, arg), (kwarg, employee_salary))
                conn.commit()
                print("\nSUCCESS")
                return False

            elif choice == 5:
                employee_gender = str(input("where employee gender: "))
                conn.execute('UPDATE {} SET {} = ? WHERE GENDER = ?'.format(table, arg), (kwarg, employee_gender))
                conn.commit()
                print("\nSUCCESS")
                return False

            elif choice == 6:
                # exit()
                return False
            else:
                print("\nINVALID")

    def delete_table_data(self):
        print("\n:: DELETE THE TABLE DATA ::")
        print("input null to delete data\n")
        table_name = str(input("Input table name: "))

        Data.delete_table_data_where(self, table_name)

    def delete_table_data_where(self, table):
        while True:
            print("\n:: CHOOSE AN OPTION ::\n")
            print("[1] -> WHERE NAME")
            print("[2] -> WHERE AGE")
            print("[3] -> WHERE ADDRESS")
            print("[4] -> WHERE SALARY")
            print("[5] -> WHERE GENDER")
            print("[6] -> BACK\n")

            choice = input("[?] -> ")

            try:
                choice = int(choice)
            except ValueError:
                print("\nINVALID")
                continue

            if choice == 1:
                employee_name = str(input("where employee name: "))
                conn.execute('DELETE FROM {} WHERE NAME = {}'.format(table, employee_name))
                conn.commit()
                print("\nSUCCESS")
                return False

            elif choice == 2:
                employee_age = int(input("where employee age: "))
                conn.execute('DELETE FROM {} WHERE AGE = {}'.format(table, employee_age))
                conn.commit()
                print("\nSUCCESS")
                return False

            elif choice == 3:
                employee_address = str(input("where employee address: "))
                conn.execute('DELETE FROM {} WHERE ADDRESS = {}'.format(table, employee_address))
                conn.commit()
                print("\nSUCCESS")
                return False

            elif choice == 4:
                employee_salary = float(input("where employee salary: "))
                conn.execute('DELETE FROM {} WHERE SALARY = {}'.format(table, employee_salary))
                conn.commit()
                print("\nSUCCESS")
                return False

            elif choice == 5:
                employee_gender = str(input("where employee gender: "))
                conn.execute('DELETE FROM {} WHERE GENDER = {}'.format(table, employee_gender))
                conn.commit()
                print("\nSUCCESS")
                return False

            elif choice == 6:
                # exit()
                return False
            else:
                print("\nINVALID")


    def select_table_data(self):
        pass
        # print("\n:: SELECT THE TABLE DATA ::")
        # print("input null to delete data\n")
        # table_name = str(input("Input table name: "))
        #
        # Data.select_table_data_set(self, table_name)

