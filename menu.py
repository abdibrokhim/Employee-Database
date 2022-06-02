import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")


class Menu:
    def menu(self):
        print("\n:: CHOOSE AN OPTION ::\n")
        print("[1] -> CREATE TABLE")
        print("[2] -> EXIT\n")

        option(self)

    def option(self):
        choice = int(input("[?] -> "))
        if choice == 1:
            create_table(self)
        elif choice == 2:
            exit()
        else:
            print("INVALID")
            menu(self)