from abc import ABC, abstractmethod
class Account(ABC):
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully")
        else:
            print(" Insufficient balance")
    def show_balance(self):
        print(f"Balance: ₹{self.balance}")
    @abstractmethod
    def account_type(self):
        pass
