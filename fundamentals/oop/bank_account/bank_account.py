class BankAccount:
    num_of_acc = 0
    acc_info = []

    def __init__(self, int_rate, balance):
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.num_of_acc += 1
        BankAccount.acc_info.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance - amount) >= 0 :
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance : {self.balance}")

    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate) 
        return self

    @classmethod
    def total_acc(cls):
        print(f"\nThere are {cls.num_of_acc} accounts")
    
    @classmethod
    def print_acc_info(cls):
        for account in cls.acc_info:
            account.display_account_info()

savings = BankAccount(0.05, 1000)
checking = BankAccount(0.02, 5000)
BankAccount.total_acc()
print("====================")
savings.deposit(10).deposit(50).deposit(150).withdraw(600).yeild_interest().display_account_info()
checking.deposit(100).deposit(200).withdraw(200).withdraw(30).withdraw(350).withdraw(1200).yeild_interest().display_account_info()
BankAccount.print_acc_info()
print("================")
# print(BankAccount.acc_info)
# print("======================================\t\t============================================")


import urllib.request
response = urllib.request.urlopen("http://www.codingdojo.com")
html = response.read()
print(html)