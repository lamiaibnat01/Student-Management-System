from modules.operations import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student
)

while True:
    print("=" * 30)
    print(" STUDENT MANAGEMENT SYSTEM")
    print("=" * 30)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("=" * 50)
        print("Thank You For Using")
        print("STUDENT MANAGEMENT SYSTEM")
        print("\nProgram Closed Successfully!")
        print("=" * 50)
        break

    else:
        print("Invalid Choice!")
