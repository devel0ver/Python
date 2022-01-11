class User:
    def __init__(self, user_data):
        self.user_name = user_data["User"]
        self.account_balance = user_data["Balance"]

    def make_deposit(self,amount):    
        self.account_balance += amount
        return self.account_balance

    def make_withdrawl(self,amount):    
        self.account_balance -= amount
        return self.account_balance


    def display_user_balance(self):
        print(f"User : {self.user_name}, Balance : {self.account_balance}")

    def transfer_money(self,other_user,amount):
        if(self.account_balance > 0 and amount <= self.account_balance):
            self.account_balance -= amount
            second_user.account_balance += amount


first_user_data = {
    "User" : "Adrien",
    "Balance" : 105,
}
first_user = User(first_user_data)

second_user_data = {
    "User" : "Mr. Nibbles",
    "Balance" : 1200,
}
second_user = User(second_user_data)

third_user_data = {
    "User" : "Benny Bob",
    "Balance" : 3300,
}
third_user = User(third_user_data)

first_user.make_deposit(200)
first_user.make_deposit(300)
first_user.make_deposit(600)
first_user.make_withdrawl(450)

second_user.make_deposit(400)
second_user.make_deposit(100)
second_user.make_withdrawl(800)
second_user.make_withdrawl(220)

third_user.make_withdrawl(1600)
third_user.make_withdrawl(930)
third_user.make_withdrawl(489)
third_user.make_deposit(370)

print("\n===========================")
first_user.display_user_balance()
second_user.display_user_balance()
third_user.display_user_balance()
print("===========================\n")

first_user.transfer_money(second_user.account_balance, 400) # I changed it a little. If you go above the amount of your balance, it will not transfer!!
first_user.display_user_balance()
second_user.display_user_balance()
print("===========================\n")