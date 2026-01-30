class StudentManagementSystem:

    def __init__(self):
        self.students = {}

    # ---------- Validation (GUI friendly) ----------
    
    def validate_id(self, sid):
        if sid == "":
            return "Student ID cannot be empty!"
        if not sid.isalnum():
            return "Student ID must contain only letters and numbers!"
        if len(sid) < 3 or len(sid) > 10:
            return "Student ID must be 3 to 10 characters long!"
        return None

    def validate_name(self, name):
        if name == "":
            return "Name cannot be empty!"
        if not all(x.isalpha() or x.isspace() for x in name):
            return "Name can contain only letters and spaces!"
        if len(name) < 3 or len(name) > 30:
            return "Name must be 3 to 30 characters long!"
        return None

    def validate_age(self, age):
        if age == "":
            return "Age cannot be empty!"
        if not age.isdigit():
            return "Age must be a number!"
        age = int(age)
        if age < 5 or age > 100:
            return "Age must be between 5 and 100!"
        return None

    # ---------- CRUD Operations ----------
    def add_student(self, sid, name, age):
        error = self.validate_id(sid) or \
                self.validate_name(name) or \
                self.validate_age(age)
        if error:
            return error

        if sid in self.students:
            return "Student already exists!"

        self.students[sid] = {"name": name, "age": int(age)}
        return "Student added successfully!"

    def view_students(self):
        if not self.students:
            return "No students found."

        result = "--- Student List ---\n"
        for sid, info in self.students.items():
            result += f"ID: {sid}, Name: {info['name']}, Age: {info['age']}\n"
        return result

    def update_student(self, sid, name, age):
        error = self.validate_id(sid) or \
                self.validate_name(name) or \
                self.validate_age(age)
        if error:
            return error

        if sid not in self.students:
            return "Student not found!"

        self.students[sid]["name"] = name
        self.students[sid]["age"] = int(age)
        return "Student updated successfully!"

    def delete_student(self, sid):
        error = self.validate_id(sid)
        if error:
            return error

        if sid not in self.students:
            return "Student not found!"

        del self.students[sid]
        return "Student deleted successfully!"
