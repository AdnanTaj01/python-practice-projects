class StudentManagementSystem:

    def __init__(self):
        self.students = {}   # same as students = {} in main()

    def show_menu(self):
        print("\n====== STUDENT MANAGEMENT SYSTEM ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

    def get_valid_choice(self):
        while True:
            choice = input("\nChoose an option (1/2/3/4/5): ")
            if choice in ['1', '2', '3', '4', '5']:
                return choice
            print("\nInvalid choice! Please select again.")

    def get_valid_id(self, message):
        while True:
            sid = input(message).strip()
            if sid == "":
                print("Student ID cannot be empty!")
            elif not sid.isalnum():
                print("Student ID must contain only letters and numbers!")
            else:
                return sid

    def get_valid_name(self, message):
        while True:
            name = input(message).strip()
            if name == "":
                print("Name cannot be empty!")
            elif not all(x.isalpha() or x.isspace() for x in name):
                print("Name can contain only letters and spaces!")
            else:
                return name

    def get_valid_age(self, message):
        while True:
            age = input(message).strip()
            if age == "":
                print("Age cannot be empty!")
            elif not age.isdigit():
                print("Age must be a number!")
            else:
                return age

    def add_student(self, sid, name, age):
        sid = self.get_valid_id("\nEnter Student ID: ")
        if sid in self.students:
            return "Student already exists!"

        name = self.get_valid_name("Enter Student Name: ")
        age = self.get_valid_age("Enter Student Age: ")

        self.students[sid] = {"name": name, "age": age}
        return "Student added successfully!"

    def view_students(self):
        if not self.students:
            return "No students found."

        result = "\n--- Student List ---\n"
        for sid, info in self.students.items():
            result += f"ID: {sid}, Name: {info['name']}, Age: {info['age']}\n"
        return result

    def update_student(self,sid, name, age):
        sid = self.get_valid_id("\nEnter Student ID to update: ")
        if sid not in self.students:
            return "Student not found!"

        name = self.get_valid_name("Enter new name: ")
        age = self.get_valid_age("Enter new age: ")

        self.students[sid]["name"] = name
        self.students[sid]["age"] = age
        return "Student updated successfully!"
    
    def delete_student(self,sid):
        sid = self.get_valid_id("\nEnter Student ID to delete: ")
        if sid not in self.students:
            return "Student not found!"

        del self.students[sid]
        return "Student deleted successfully!"

    def perform_operation(self, choice):
        if choice == '1':
            return self.add_student()
        elif choice == '2':
            return self.view_students()
        elif choice == '3':
            return self.update_student()
        elif choice == '4':
            return self.delete_student()
        elif choice == '5':
            return "exit"

    def run(self):
        while True:
            self.show_menu()
            choice = self.get_valid_choice()

            result = self.perform_operation(choice)

            if result == "exit":
                print("\nThank you for using Student Management System!")
                break

            print("\nResult:", result)


# if __name__ == "__main__":
#     sms = StudentManagementSystem()
#     sms.run()
