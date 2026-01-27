def show_menu():
    print("\n====== SMART CALCULATOR ======")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")


def get_valid_choice():
    while True:
        choice = input("Choose an operation (1/2/3/4): ")
        if choice in ['1', '2', '3', '4']:
            return choice
        print("Invalid choice! Please select again.")


def get_valid_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input! Please enter a number.")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def perform_operation(choice, num1, num2):
    if choice == '1':
        return add(num1, num2)
    elif choice == '2':
        return subtract(num1, num2)
    elif choice == '3':
        return multiply(num1, num2)
    elif choice == '4':
        return divide(num1, num2)


def ask_to_continue():
    while True:
        answer = input("\nDo you want to calculate again? (yes/no): ").lower()
        if answer in ['yes', 'no']:
            return answer == 'yes'
        print("Please type 'yes' or 'no'.")


def main():
    while True:
        show_menu()
        choice = get_valid_choice()

        num1 = get_valid_number("\nEnter first number: ")
        num2 = get_valid_number("\nEnter second number: ")

        result = perform_operation(choice, num1, num2)
        print("Result:", result)

        if not ask_to_continue():
            print("Thank you for using Smart Calculator!")
            break


if __name__ == "__main__":
    main()