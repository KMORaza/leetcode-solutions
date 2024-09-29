class Bank:
    def __init__(self, initial_amounts):
        self.accounts = initial_amounts
    def transfer(self, from_account, to_account, transfer_amount):
        if not self.is_account_valid(to_account):
            return False
        return self.withdraw(from_account, transfer_amount) and self.deposit(to_account, transfer_amount)
    def deposit(self, account, deposit_amount):
        if not self.is_account_valid(account):
            return False
        self.accounts[account - 1] += deposit_amount
        return True
    def withdraw(self, account, withdrawal_amount):
        if not self.is_account_valid(account):
            return False
        if self.accounts[account - 1] < withdrawal_amount:
            return False
        self.accounts[account - 1] -= withdrawal_amount
        return True
    def is_account_valid(self, account):
        return 1 <= account <= len(self.accounts)
