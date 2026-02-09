# 💰 Expense Tracker CLI

A Professional Python Command-Line Expense Management System


## 📌 Overview

**Expense Tracker CLI** is a structured and production-ready command-line application built with Python.
It allows users to efficiently manage daily expenses using a CSV-based storage system with proper validation and error handling.

The project demonstrates clean architecture, modular design, file handling, and robust input validation — making it suitable for portfolio and GitHub showcase.



## ✨ Key Features

* ✔ Add expenses with automatic date stamping
* ✔ View all expenses in formatted table view
* ✔ Calculate total expenses dynamically
* ✔ Search expenses by category (case-insensitive)
* ✔ Delete expenses by category (with confirmation)
* ✔ Delete all records securely
* ✔ Automatic folder & file creation
* ✔ Corrupted row handling
* ✔ Exception handling & validation






### Design Principles Used

* Modular function-based structure
* Separation of concerns
* Defensive programming
* Clean input validation
* Safe file operations




## 🖥 Application Menu


========================================
💰 EXPENSE TRACKER
========================================
1. Add Expense
2. View Expenses
3. Search by Category
4. Delete by Category
5. Delete All
6. Exit






## 🛡 Error Handling Strategy

* FileNotFoundError protection
* PermissionError handling
* Input validation loops
* Corrupted CSV row skipping
* Safe confirmation before deletion


## 📊 Sample Output

========================================
💰 EXPENSE TRACKER
========================================
1. Add Expense
2. View Expenses
3. Search by Category
4. Delete Expenses by Category
5. Delete All Expenses
6. Exit
Choose option (1-6): 2


Date         Category        Amount     Description
------------------------------------------------------------
2026-02-09   Transport       500.00     Bus fare
2026-02-09   Food            1200.00    Dinner with friends
2026-02-09   Bills           3000.00    Electricity bill
2026-02-09   Mobile          1000.00    Mobile package
2026-02-09   Internet        2500.00    Monthly WiFi
2026-02-09   Shopping        4500.00    Clothes
2026-02-09   Medicine        800.00     Pharmacy
2026-02-09   Petrol          4000.00    Bike fuel
2026-02-09   Snacks          600.00     Lays & drinks
2026-02-09   Education       7000.00    Course fee
2026-02-09   Entertainment   1500.00    Cinema
2026-02-09   Maintenance     2000.00    Bike service
2026-02-09   Gift            1800.00    Birthday gift
2026-02-09   Laundry         900.00     Clothes washing
2026-02-09   Rent            15000.00   Monthly rent
2026-02-09   Water Bill      1200.00    Monthly water bill
2026-02-09   Charity         1000.00    Donation
2026-02-09   Subscription    800.00     Netflix
2026-02-09   Stationery      650.00     Office supplies2026-02-09
2026-02-09   Food            2000.00    weekly fruits
------------------------------------------------------------
💰 Total Expenses: 51950.00

========================================
💰 EXPENSE TRACKER
========================================
1. Add Expense
2. View Expenses
3. Search by Category
4. Delete Expenses by Category
5. Delete All Expenses
6. Exit
Choose option (1-6): 3

Enter category to search: Food

Date         Category        Amount     Description
------------------------------------------------------------
2026-02-09   Food            1200.00    Dinner with friends
2026-02-09   Food            2000.00    weekly fruits
------------------------------------------------------------
Total for food: 3200.00

========================================
💰 EXPENSE TRACKER
========================================
1. Add Expense
2. View Expenses
3. Search by Category
4. Delete Expenses by Category
5. Delete All Expenses
6. Exit
Choose option (1-6): 4

Enter category to delete: Food

Are you sure you want to delete 2 record(s) of 'food'? (yes/no): yes

✅ 2 record(s) deleted successfully

========================================
💰 EXPENSE TRACKER
========================================
1. Add Expense
2. View Expenses
3. Search by Category
4. Delete Expenses by Category
5. Delete All Expenses
6. Exit
Choose option (1-6): 2

Date         Category        Amount     Description
------------------------------------------------------------
2026-02-09   Transport       500.00     Bus fare
2026-02-09   Bills           3000.00    Electricity bill
2026-02-09   Mobile          1000.00    Mobile package
2026-02-09   Internet        2500.00    Monthly WiFi
2026-02-09   Shopping        4500.00    Clothes
2026-02-09   Medicine        800.00     Pharmacy
2026-02-09   Petrol          4000.00    Bike fuel
2026-02-09   Snacks          600.00     Lays & drinks
2026-02-09   Education       7000.00    Course fee
2026-02-09   Entertainment   1500.00    Cinema
2026-02-09   Maintenance     2000.00    Bike service
2026-02-09   Gift            1800.00    Birthday gift
2026-02-09   Laundry         900.00     Clothes washing
2026-02-09   Rent            15000.00   Monthly rent
2026-02-09   Water Bill      1200.00    Monthly water bill
2026-02-09   Charity         1000.00    Donation
2026-02-09   Subscription    800.00     Netflix
2026-02-09   Stationery      650.00     Office supplies2026-02-09
------------------------------------------------------------
💰 Total Expenses: 48750.00

========================================
💰 EXPENSE TRACKER
========================================
1. Add Expense
2. View Expenses
3. Search by Category
4. Delete Expenses by Category
5. Delete All Expenses
6. Exit
Choose option (1-6): 6

Goodbye! Happy Saving!


## 🎯 Learning Outcomes

This project demonstrates:

* File Handling
* CSV Data Management
* Exception Handling
* Defensive Programming
* CLI Application Design
* Real-world Project Structuring



