from table import Table


def main():
    table = Table()
    c = 0

    while True:
        if c < 1:
            print("\nWELCOME")
        print("\n:: CHOOSE AN OPTION ::\n")
        print("[1] -> CREATE NEW TABLE")
        print("[2] -> DELETE TABLE")
        print("[3] -> SHOW ALL TABLES")
        print("[4] -> MORE")
        print("[5] -> EXIT\n")

        choice = input("[?] -> ")

        try:
            choice = int(choice)
        except ValueError:
            print("\nINVALID")
            continue

        if choice == 1:
            table.create_table()
            c += 1
        elif choice == 2:
            table.delete_table()
            c += 1
        elif choice == 3:
            table.show_table()
            c += 1
        elif choice == 4:
            table.show_more()
            c += 1
        elif choice == 5:
            exit()
        else:
            print("\nINVALID")
            c += 1

    print("\nBYE\n")


if __name__ == '__main__':
    main()
