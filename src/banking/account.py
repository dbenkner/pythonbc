class Account:
    def __init__(self, description):
        self._next_account_num = 1
        self._description = description
        self._routing_num = "123 456 789"
        self._balance = 0
        
    @property
    def account_num(self):
        return self._account_num
    @account_num.setter
    def set_account_num(self, next_account_num):
        self._account_num = next_account_num
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def set_balance(self, amount):
        self._balance = amount
    @property
    def next_acount_no(self):
        return self._next_account_num
    @next_acount_no.setter
    def set_next_account_no(self):
        self._next_account_num = set._next_account_num + 1
    
    
        
class Savings(Account):
    def __init__(self, account_no, balance, description):
        self._account_no = account_no
        self._balance = balance
        self._description = description
        self._routing_num = "123 456 789"
        self._interest_rate = .1