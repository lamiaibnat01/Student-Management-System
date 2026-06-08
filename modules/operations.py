from modules.student import Student
from modules.grades import calculate_grade

FILE_PATH = "data/students.txt"


def add_student():

    print("=" * 50)
    print("ADD STUDENT")
    print("=" * 50)

    name = input("Enter Student Name  : ")
    age = input("Enter Student Age   : ")
    marks = input("Enter Student Marks : ")

    student = Student(name, age, marks)

    with open(FILE_PATH, "a") as file:
        file.write(str(student) + "\n")

    print("\nStudent Added Successfully!")
    print("=" * 50)


def view_students():

    print("=" * 50)
    print("STUDENT LIST")
    print("=" * 50)

    try:
        with open(FILE_PATH, "r") as file:
            students = file.readlines()

        print(f"{'Name':20} {'Age':10} {'Marks':10} {'Grade'}")
        print("-" * 50)

        count = 0

        for student in students:
            data = student.strip().split(",")

            if len(data) == 3:
                name, age, marks = data
                grade = calculate_grade(int(marks))

                print(
                    f"{name:20} {age:10} {marks:10} {grade}"
                )

                count += 1

        print("=" * 50)
        print(f"Total Students: {count}")
        print("=" * 50)

    except FileNotFoundError:
        print("No Student Data Found!")


def search_student():

    print("=" * 50)
    print("SEARCH STUDENT")
    print("=" * 50)

    search_name = input("Enter Student Name: ")

    try:
        with open(FILE_PATH, "r") as file:

            found = False

            for student in file:
                name, age, marks = student.strip().split(",")

                if search_name.lower() in name.lower():

                    print("\nStudent Found!")
                    print("-" * 50)
                    print(f"Name  : {name}")
                    print(f"Age   : {age}")
                    print(f"Marks : {marks}")
                    print(
                        f"Grade : {calculate_grade(int(marks))}"
                    )

                    found = True
                    break

            if not found:
                print("Student Not Found!")

    except FileNotFoundError:
        print("No Student Data Found!")


def update_student():

    print("=" * 50)
    print("UPDATE STUDENT")
    print("=" * 50)

    search_name = input("Enter Student Name: ")

    try:
        with open(FILE_PATH, "r") as file:
            students = file.readlines()

        updated = False

        with open(FILE_PATH, "w") as file:

            for student in students:

                name, age, marks = student.strip().split(",")

                if search_name.lower() == name.lower():

                    print("\nCurrent Information")
                    print("-" * 50)
                    print(f"Name  : {name}")
                    print(f"Age   : {age}")
                    print(f"Marks : {marks}")

                    new_name = input("\nEnter New Name   : ")
                    new_age = input("Enter New Age    : ")
                    new_marks = input("Enter New Marks  : ")

                    file.write(
                        f"{new_name},{new_age},{new_marks}\n"
                    )

                    updated = True

                else:
                    file.write(student)

        if updated:
            print("\nStudent Updated Successfully!")
        else:
            print("Student Not Found!")

    except FileNotFoundError:
        print("No Student Data Found!")


def delete_student():

    print("=" * 50)
    print("DELETE STUDENT")
    print("=" * 50)

    search_name = input("Enter Student Name: ")

    try:
        with open(FILE_PATH, "r") as file:
            students = file.readlines()

        deleted = False

        with open(FILE_PATH, "w") as file:

            for student in students:

                name, age, marks = student.strip().split(",")

                if search_name.lower() == name.lower():
                    deleted = True
                    continue

                file.write(student)

        if deleted:
            print("Student Deleted Successfully!")
        else:
            print("Student Not Found!")

    except FileNotFoundError:
        print("No Student Data Found!")
