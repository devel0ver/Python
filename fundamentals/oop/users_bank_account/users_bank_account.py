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
        return f"{self.balance}"

    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate) 
        return self

    @classmethod
    def print_acc_info(cls):
        for account in cls.acc_info:
            account.display_account_info()


class User:
    # Class attribute

    # ! CONSTRUCTOR FUNCTION!! CREATES THE INSTANCE OF AN OBJECT
    def __init__(self, name):
        self.user_name = name
        self.account = {
            "savings" : BankAccount(.04, 1500),
            "checking" : BankAccount(0.15, 2600)
            }


    def display_user_balance(self):
        print(f"User : {self.user_name}, Savings Balance : {self.account['savings'].display_account_info()}")
        print(f"User : {self.user_name}, Checking Balance : {self.account['checking'].display_account_info()}")

    # def transfer_money(self,other_user,amount):
    #     if(self.account_balance > 0 and amount <= self.account_balance):
    #         self.account_balance -= amount
    #         second_user.account_balance += amount

shaya = User("Shaya")
shaya.account['savings'].deposit(100)
shaya.account['checking'].deposit(100)
shaya.display_user_balance()