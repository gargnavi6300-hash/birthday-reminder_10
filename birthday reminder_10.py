# Birthday Reminder Project

birthdays = {
    "Rahul": "28/09",
    "Ananya": "02/10",
    "Riya": "15/11"
}


def display_birthdays():
    print("\n--- ALL BIRTHDAYS ---")

    count = 0

    for name, date in birthdays.items():
        print(name, ":", date)
        count = count + 1

    print("Total birthdays:", count)


def add_birthday():
    name = input("\nEnter person's name: ")
    date = input("Enter birthday (DD/MM): ")

    birthdays[name] = date

    print("Birthday added successfully!")


def search_birthday():
    name = input("\nEnter name to search: ")

    if name in birthdays:
        print(name, "'s birthday is on", birthdays[name])
    else:
        print("Birthday not found.")


def check_today():
    today = input("\nEnter today's date (DD/MM): ")

    found = False

    for name, date in birthdays.items():
        if date == today:
            print("Birthdays today:", name)
            found = True

    if found == False:
        print("No birthday today.")


while True:
    print("\n================================")
    print("       BIRTHDAY REMINDER")
    print("================================")
    print("1. Add Birthday")
    print("2. Display All Birthdays")
    print("3. Search Birthday")
    print("4. Check Today's Birthday")
    print("5. Exit")
    print("================================")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_birthday()

    elif choice == 2:
        display_birthdays()

    elif choice == 3:
        search_birthday()

    elif choice == 4:
        check_today()

    elif choice == 5:
        print("\nThank you for using Birthday Reminder!")
        break

    else:
        print("\nInvalid choice. Please try again.")