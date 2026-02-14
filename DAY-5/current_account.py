from account import Account
class CurrentAccount(Account):
    def account_type(self):
        return "Current Account"
    def withdraw(self, amount):
        if amount <= self.balance + 5000:
            self.balance -= amount
            print(f"₹{amount} withdrawn (Overdraft allowed)")
        else:
            print("❌ Overdraft limit exceeded")
