import sqlite3

from menu import Menu

conn = sqlite3.connect('test.db')
print("Opened database successfully")\


class Main:
    def __init__(self, table_name, employee_name, employee_age, employee_address, employee_salary, employee_gender):
        self.table_name = table_name
        self.employee_name = employee_name
        self.employee_age = employee_age
        self.employee_address = employee_address
        self.employee_salary = employee_salary
        self.employee_gender = employee_gender


    def main(self):
        print("WELCOME")
        Menu.menu()

    def create_table(table_name):
        conn.execute(f'''CREATE TABLE {table_name}
                 (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
                 NAME           TEXT         NOT NULL,
                 AGE            INT          NOT NULL,
                 ADDRESS        CHAR(50),
                 SALARY         REAL);''')
        print("Table created successfully")

        conn.close()

        add_table()


if __name__ == '__main__':
    Main()
