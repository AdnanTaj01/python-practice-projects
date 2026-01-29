import tkinter as tk
from tkinter import messagebox
from calculatorOop import Calculator   # CLI class import


class CalculatorGUI:
    def __init__(self, root):
        
        self.calc = Calculator()   # Calculator class  object
        self.root = root
        self.root.title("Smart Calculator")
        self.root.geometry("350x300")

        tk.Label(root, text="SMART CALCULATOR", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(root, text="First Number").pack()
        
        self.num1 = tk.Entry(root)
        self.num1.pack()

        tk.Label(root, text="Second Number").pack()
        
        self.num2 = tk.Entry(root)
        self.num2.pack()

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="+", width=6, command=lambda: self.calculate('1')).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="-", width=6, command=lambda: self.calculate('2')).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="×", width=6, command=lambda: self.calculate('3')).grid(row=1, column=0, padx=5)
        tk.Button(btn_frame, text="÷", width=6, command=lambda: self.calculate('4')).grid(row=1, column=1, padx=5)

        self.result = tk.Label(root, text="Result: ", font=("Arial", 12))
        self.result.pack(pady=10)

    def calculate(self, choice):
        try:
            a = float(self.num1.get())
            b = float(self.num2.get())
            result = self.calc.perform_operation(choice, a, b)
            self.result.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")


# GUI Run
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()
