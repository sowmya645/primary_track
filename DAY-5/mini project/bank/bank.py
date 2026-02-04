class Bank:
    def __init__(self, name):
        self.bank_name = name
        self.__accounts = {}  
    def add_account(self, account):
        self.__accounts[account.account_no] = account

    def get_account(self, acc_no):
        return self.__accounts.get(acc_no, None)
