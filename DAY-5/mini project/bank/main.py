from bank import Bank
from savings_account import SavingsAccount
from current_account import CurrentAccount
bank = Bank("Python Bank")
acc1 = SavingsAccount(101, "sasi", 5000)
acc2 = CurrentAccount(102, "Anu", 10000)
bank.add_account(acc1)
bank.add_account(acc2)
account = bank.get_account(101)
print("\nAccount Type:", account.account_type())
account.deposit(2000)
account.withdraw(1000)
account.show_balance()
print("\n Current Account ")
account2 = bank.get_account(102)
print("Account Type:", account2.account_type())
account2.withdraw(13000)
account2.show_balance()
