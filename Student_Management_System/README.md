# Student Management System (SMS) - Python CLI

A simple **Command-Line Interface (CLI)** based Student Management System implemented in Python.  
This project allows users to **add, view, update, and delete student records** with proper input validation and professional structure.

---

## Features

- **Add Student**  
  - Store Student ID, Name, and Age
  - Validates ID to be **alphanumeric**
  - Validates Name to contain **letters and spaces only**
  - Validates Age to be **numeric**

- **View Students**  
  - Lists all students in a clear format  
  - Shows ID, Name, and Age  

- **Update Student**  
  - Update existing student details  
  - Validates updated Name and Age  

- **Delete Student**  
  - Remove a student by ID  
  - Confirms if student exists before deletion  

- **Exit Option**  
  - Clean exit from the program  

---

# OUTPUT


====== STUDENT MANAGEMENT SYSTEM ======
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit

Choose an option (1/2/3/4/5): 6

Invalid choice! Please select again.

Choose an option (1/2/3/4/5): d

Invalid choice! Please select again.

Choose an option (1/2/3/4/5): 2

Result: No students found.

====== STUDENT MANAGEMENT SYSTEM ======
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit

Choose an option (1/2/3/4/5): 1

Enter Student ID: 4439FOC
Enter Student Name: Adnan Taj
Enter Student Age: 23

Result: Student added successfully!

====== STUDENT MANAGEMENT SYSTEM ======
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit

Choose an option (1/2/3/4/5): 2

Result:
--- Student List ---
ID: 4439FOC, Name: Adnan Taj, Age: 23


====== STUDENT MANAGEMENT SYSTEM ======
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit

Choose an option (1/2/3/4/5): 1

Enter Student ID: 1122AOA
Enter Student Name: Wajid Taj
Enter Student Age: 20

Result: Student added successfully!

====== STUDENT MANAGEMENT SYSTEM ======
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit

Choose an option (1/2/3/4/5): 2

Result:
--- Student List ---
ID: 4439FOC, Name: Adnan Taj, Age: 23
ID: 1122AOA, Name: Wajid Taj, Age: 20


====== STUDENT MANAGEMENT SYSTEM ======
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit

Choose an option (1/2/3/4/5): 1

Enter Student ID: 222AAA
Enter Student Name: Khalid Taj
Enter Student Age: 28

Result: Student added successfully!

====== STUDENT MANAGEMENT SYSTEM ======
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit

Choose an option (1/2/3/4/5): 2

Result:
--- Student List ---
ID: 4439FOC, Name: Adnan Taj, Age: 23
ID: 1122AOA, Name: Wajid Taj, Age: 20
ID: 222AAA, Name: Khalid Taj, Age: 28


====== STUDENT MANAGEMENT SYSTEM ======
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit

Choose an option (1/2/3/4/5): 3

Enter Student ID to update: 1122AOA
Enter new name: Rehman Taj
Enter new age: 34

Result: Student updated successfully!

====== STUDENT MANAGEMENT SYSTEM ======
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit

Choose an option (1/2/3/4/5): 2

Result:
--- Student List ---
ID: 4439FOC, Name: Adnan Taj, Age: 23
ID: 1122AOA, Name: Rehman Taj, Age: 34
ID: 222AAA, Name: Khalid Taj, Age: 28


====== STUDENT MANAGEMENT SYSTEM ======
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit

Choose an option (1/2/3/4/5): 4

Enter Student ID to delete: 1122AOA

Result: Student deleted successfully!

====== STUDENT MANAGEMENT SYSTEM ======
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit

Choose an option (1/2/3/4/5): 2

Result:
--- Student List ---
ID: 4439FOC, Name: Adnan Taj, Age: 23
ID: 222AAA, Name: Khalid Taj, Age: 28


====== STUDENT MANAGEMENT SYSTEM ======
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit

Choose an option (1/2/3/4/5): 1

Enter Student ID: q
Enter Student Name: 1
Name can contain only letters and spaces!
Enter Student Name: @
Name can contain only letters and spaces!
Enter Student Name: Wajid
Enter Student Age: a
Age must be a number!
Enter Student Age: @
Age must be a number!
Enter Student Age: 12

Result: Student added successfully!

====== STUDENT MANAGEMENT SYSTEM ======
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit

Choose an option (1/2/3/4/5): 5

Thank you for using Student Management System!



