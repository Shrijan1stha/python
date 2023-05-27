from create_student import create
from read_student import read
from update_student import update
from delete_student import delete


def inquiry():
    selection = input("Enter your choice C/R/U/D ")
    selection = selection.lower()

    def exit_message():
        print("Thank you. See you again !!")

    if selection == 'c':
        contd = create()
        inquiry() if contd else exit_message()
    elif selection == 'r':
        id = input("Enter student id ")
        contd = read(id)
        inquiry() if contd else exit_message()
    elif selection == 'u':
        id = input("Enter student id ")
        to_change = input("Enter info you want to change ")
        if to_change.lower() not in ["name", "age"]:
            print("Invalid student info")
            exit_message()
        else:
            changed_value = input(f"Enter new {to_change} ")
            contd = update(id, to_change, changed_value)
            inquiry() if contd else exit_message()

    elif selection == 'd':
        choice = input("Delete all or give student id (a / id): ")
        if choice.lower() == 'a':
            contd = delete('a')
        else:
            id = input("Enter student id: ")
            contd = delete(id)
            inquiry() if contd else exit_message()
    else:
        print("Invalid Choice !!")


if __name__ == "__main__":
    inquiry()
