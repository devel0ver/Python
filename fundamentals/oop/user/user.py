class User:
    # Class attribute
    amount_of_users = 0
    bank_name = "First National Dojo"

    # ! CONSTRUCTOR FUNCTION!! CREATES THE INSTANCE OF AN OBJECT
    def __init__(self, user_data):
        self.user_name = user_data["User"]
        self.account_balance = user_data["Balance"]
        User.amount_of_users += 1

    def make_deposit(self,amount):    
        self.account_balance += amount
        return self

    def make_withdrawl(self,amount):    
        self.account_balance -= amount
        return self


    def display_user_balance(self):
        print(f"User : {self.user_name}, Balance : {self.account_balance}")

    def transfer_money(self,other_user,amount):
        if(self.account_balance > 0 and amount <= self.account_balance):
            self.account_balance -= amount
            second_user.account_balance += amount

    @classmethod
    def money_holders(cls):
        print(f"There are {cls.amount_of_users} users")
        
    @classmethod
    def change_bank_name(cls, name):
        cls.change_bank_name = name
        print(name)



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

first_user.make_deposit(200).make_deposit(300).make_deposit(600).make_withdrawl(450)

second_user.make_deposit(400).make_deposit(100).make_withdrawl(800).make_withdrawl(220)

third_user.make_withdrawl(1600).make_withdrawl(930).make_withdrawl(489).make_deposit(370)

name = "The Bank Of Aden"
print("\n===========================")
User.change_bank_name(name)
print("===========================")
User.money_holders()
first_user.display_user_balance()
second_user.display_user_balance()
third_user.display_user_balance()
print("===========================")
first_user.transfer_money(second_user.account_balance, 400) # I changed it a little. If you go above the amount of your balance, it will not transfer!!
print("Transferred Money:")
first_user.display_user_balance()
second_user.display_user_balance()
print("===========================")



