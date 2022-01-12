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
            print("Insufficient Funds")
        return self

    def display_account_info(self):
        print(f"Balance : {self.balance}")

    def yeild_interest(self):
        self.balance = (self.balance + self.balance) * self.int_rate
        return self

    @classmethod
    def total_acc(cls):
        print(f"\nThere are {cls.num_of_acc} accounts")

first_acc = BankAccount(0.30, 0)
second_acc = BankAccount(0.30, 0)
BankAccount.total_acc()
print("====================")
first_acc.deposit(950).deposit(950).deposit(835).withdraw(1900).yeild_interest()
first_acc.display_account_info()
print("================")
second_acc.deposit(2000).deposit(1450).withdraw(833).withdraw(500).withdraw(350).withdraw(1200).yeild_interest()
second_acc.display_account_info()
print("================")
print(BankAccount.acc_info)
print("======================================\t\t============================================")