class bankaccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
    def show_details(self):
        print(self.account_holder)
        print(self.balance)
class savingsaccount(bankaccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate
class currentaccount(bankaccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit
savingsaccount = savingsaccount("Alice", 1000, 0.05)
currentaccount = currentaccount("Bob", 2000, 500)   
savingsaccount.show_details()
currentaccount.show_details()