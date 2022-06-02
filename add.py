import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")


class Add:
    def add_table(self):
        print("\n:: FILL IN THE TABLE ::")
        print("input 0 to leave blank\n")
        employee_name = str(input("Input employee name: "))
        employee_age = int(input("Input employee age: "))
        employee_address = str(input("Input employee address: "))
        employee_salary = float(input("Input employee salary: "))
        employee_gender = str(input("Input employee gender: "))