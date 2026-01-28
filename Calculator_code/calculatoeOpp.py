class Calculator:

    def show_menu(self):
        print("\n====== SMART CALCULATOR ======")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

    def get_valid_choice(self):
        while True:
            choice = input("Choose an operation (1/2/3/4): ")
            if choice in ['1', '2', '3', '4']:
                return choice
            print("❌ Invalid choice! Please select again.")

    def get_valid_number(self, message):
        while True:
            try:
                return float(input(message))
            except ValueError:
                print("❌ Invalid input! Please enter a number.")

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "❌ Error: Division by zero is not allowed."
        return a / b

    def perform_operation(self, choice, num1, num2):
        if choice == '1':
            return self.add(num1, num2)
        elif choice == '2':
            return self.subtract(num1, num2)
        elif choice == '3':
            return self.multiply(num1, num2)
        elif choice == '4':
            return self.divide(num1, num2)

    def ask_to_continue(self):
        while True:
            answer = input("Do you want to calculate again? (yes/no): ").lower()
            if answer in ['yes', 'no']:
                return answer == 'yes'
            print("❌ Please type 'yes' or 'no'.")

    def run(self):
        while True:
            self.show_menu()
            choice = self.get_valid_choice()

            num1 = self.get_valid_number("Enter first number: ")
            num2 = self.get_valid_number("Enter second number: ")

            result = self.perform_operation(choice, num1, num2)
            print("Result:", result)

            if not self.ask_to_continue():
                print("👋 Thank you for using Smart Calculator!")
                break


# Program execution starts here
calculator = Calculator()
calculator.run()
