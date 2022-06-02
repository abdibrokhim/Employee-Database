import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")


class Employee:
    def __init__(self, table_name, employee_name, employee_age, employee_address, employee_salary, employee_gender):
        self.table_name = table_name
        self.employee_name = employee_name
        self.employee_age = employee_age
        self.employee_address = employee_address
        self.employee_salary = employee_salary
        self.employee_gender = employee_gender