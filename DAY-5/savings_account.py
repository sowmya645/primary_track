from account import Account
class SavingsAccount(Account):
    def account_type(self):
        return "Savings Account"
    def add_interest(self):
        interest = self.balance * 0.04
        self.balance += interest
        print("Interest added")
