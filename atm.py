import tkinter as tk
from tkinter import messagebox

# ATM Class Definition
class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. Current balance: {self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. Current balance: {self.balance}"
        else:
            return "Insufficient funds."

# GUI Functionality
def create_gui():
    atm = ATM()

    # Function to check balance
    def check_balance():
        messagebox.showinfo("Balance", f"Current Balance: {atm.check_balance()}")

    # Function to deposit money
    def deposit():
        try:
            amount = float(entry_amount.get())
            messagebox.showinfo("Deposit", atm.deposit(amount))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    # Function to withdraw money
    def withdraw():
        try:
            amount = float(entry_amount.get())
            result = atm.withdraw(amount)
            if result == "Insufficient funds.":
                messagebox.showwarning("Warning", result)
            else:
                messagebox.showinfo("Withdraw", result)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    # Main window
    window = tk.Tk()
    window.title("ATM Machine")
    window.geometry("300x250")
    window.configure(bg="#f0f0f0")

    # Title label
    label_title = tk.Label(window, text="ATM Machine", font=("Arial", 16, "bold"), bg="#f0f0f0")
    label_title.pack(pady=10)

    # Amount Entry
    entry_amount = tk.Entry(window, width=20, font=("Arial", 12))
    entry_amount.pack(pady=10)
    entry_amount.insert(0, "Enter amount")

    # Buttons
    btn_check = tk.Button(window, text="Check Balance", width=20, command=check_balance)
    btn_check.pack(pady=5)

    btn_deposit = tk.Button(window, text="Deposit", width=20, command=deposit)
    btn_deposit.pack(pady=5)

    btn_withdraw = tk.Button(window, text="Withdraw", width=20, command=withdraw)
    btn_withdraw.pack(pady=5)

    btn_exit = tk.Button(window, text="Exit", width=20, command=window.quit)
    btn_exit.pack(pady=5)

    # Run GUI loop
    window.mainloop()

# Run the GUI
if __name__ == "__main__":
    create_gui()
