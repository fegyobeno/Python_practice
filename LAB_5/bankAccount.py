class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance
    
    @staticmethod
    def print_balance(account):
        print(account.get_balance())
    
# __var -> private variable
account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
BankAccount.print_balance(account)  # Output: 120