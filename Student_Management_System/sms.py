def show_menu():
    print("\n====== STUDENT MANAGEMENT SYSTEM ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")


def get_valid_choice():
    while True:
        choice = input("\nChoose an option (1/2/3/4/5): ")
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        print("\nInvalid choice! Please select again.")


def get_valid_id(message):
    while True:
        sid = input(message).strip()
        if sid == "":
            print("Student ID cannot be empty!")
        elif not sid.isalnum():
            print("Student ID must contain only letters and numbers!")
        else:
            return sid


def get_valid_name(message):
    while True:
        name = input(message).strip()
        if name == "":
            print("Name cannot be empty!")
        elif not all(x.isalpha() or x.isspace() for x in name):
            print("Name can contain only letters and spaces!")
        else:
            return name


def get_valid_age(message):
    while True:
        age = input(message).strip()
        if age == "":
            print("Age cannot be empty!")
        elif not age.isdigit():
            print("Age must be a number!")
        else:
            return age


def add_student(students):
    sid = get_valid_id("\nEnter Student ID: ")
    if sid in students:
        return "Student already exists!"

    name = get_valid_name("Enter Student Name: ")
    age = get_valid_age("Enter Student Age: ")

    students[sid] = {"name": name, "age": age}
    return "Student added successfully!"


def view_students(students):
    if not students:
        return "No students found."

    result = "\n--- Student List ---\n"
    for sid, info in students.items():
        result += f"ID: {sid}, Name: {info['name']}, Age: {info['age']}\n"
    return result


def update_student(students):
    sid = get_valid_id("\nEnter Student ID to update: ")
    if sid not in students:
        return "Student not found!"

    name = get_valid_name("Enter new name: ")
    age = get_valid_age("Enter new age: ")

    students[sid]["name"] = name
    students[sid]["age"] = age
    return "Student updated successfully!"


def delete_student(students):
    sid = get_valid_id("\nEnter Student ID to delete: ")
    if sid not in students:
        return "Student not found!"

    del students[sid]
    return "Student deleted successfully!"


def perform_operation(choice, students):
    if choice == '1':
        return add_student(students)
    elif choice == '2':
        return view_students(students)
    elif choice == '3':
        return update_student(students)
    elif choice == '4':
        return delete_student(students)
    elif choice == '5':
        return "exit"


def main():
    students = {}  # Professional: data inside main

    while True:
        show_menu()
        choice = get_valid_choice()

        result = perform_operation(choice, students)

        if result == "exit":
            print("\nThank you for using Student Management System!")
            break

        print("\nResult:", result)


if __name__ == "__main__":
    main() 