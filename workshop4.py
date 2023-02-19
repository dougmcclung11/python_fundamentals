class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, new_name):
        self.name = new_name

    def change_pin(self, new_pin):
        self.pin = new_pin

    def change_password(self, new_password):
        self.password = new_password


class BankUser(User):
    # BankUser constructor method
    def __init__(self, name, pin, password,):
        super().__init__(name, pin, password)
        self.balance = 0
    # Method used to display balance

    def show_balance(self):
        return f"{self.name} has an account balance of: {self.balance}"
    # Method used to withdraw an amount from balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"{self.name} has an account balance of: {self.balance}"
        else:
            print("Insufficient balance. Withdrawl not possible.")
    # Method used to deposit an amount to the balance

    def deposit(self, amount):
        self.balance += amount
        return f"{self.name} has an account balance of: {self.balance}"
    # Method used to transfer money from one user to another

    def transfer_money(self, amount, pin):
        print("You are transferring $500 to Bob")
        print("Authentication Required.")
        transfer_money_pin = int(input("Enter your PIN: "))
        if transfer_money_pin == self.pin and self.balance >= amount:
            self.balance -= amount
            self.balance += amount
            return True
        elif transfer_money_pin != self.pin:
            print("Invalid PIN, transfer canceled.")
            print(user2.show_balance())
            print(f"{user1.show_balance()}\n")
            return False
        elif self.balance > amount:
            print("Insufficient balance")
            print(user2.show_balance())
            print(f"{user1.show_balance()}\n")
            return False
    # Method used to request money from another user

    def request_money(self, amount, pin, password):
        print("You are requesting $250 from Bob.")
        print("User authentication is required...")
        request_money_pin = int(input("Enter Bob's PIN: "))
        user_password = input("Enter your password: ")
        if request_money_pin == user1.pin and user_password == user2.password:
            self.balance -= amount
            self.balance += amount
            return True
        elif request_money_pin != user1.pin:
            print("Invalid PIN. Transfer canceled.")
            print(user2.show_balance())
            print(f"{user1.show_balance()}\n")
            return False
        elif user_password != user2.password:
            print("Invalid password. Transfer canceled.")
            print(user2.show_balance())
            print(f"{user1.show_balance()}\n")
            return False
        else:
            return False


'''Driver Code for Task 1'''
'''
# Instantiating an object from the User class and printing its attributes
user1 = User("Bob", 1234, "password")
print(user1.name, user1.pin, user1.password)
'''

'''Driver Code for Task 2'''
'''
# Instantiating an object from the User class and printing its attributes
user1 = User("Bob", 1234, "password")
print(user1.name, user1.pin, user1.password)
# Changing the attributes of the previously instantiated object
user1.change_name("Bobby")
user1.change_pin(4321)
user1.change_password("newpassword")
print(user1.name, user1.pin, user1.password)
'''

'''Driver Code for Task 3'''
'''
# Instantiating an object from the BankUser subclass and printing its attributes
user1 = BankUser("Bob", 1234, "password")
print(user1.name, user1.pin, user1.password, user1.balance)
'''
'''Driver Code for Task 4'''
'''
# Instantiating an object from the BankUser subclass and printing its attributes
user1 = BankUser("Bob", 1234, "password")
# Printing the user1 object account information using the subclass methods
print(user1.show_balance())
print(user1.deposit(1000))
print(user1.withdraw(500))
'''
'''Driver Code for Task 5'''
'''
# Instantiating two objects from the BankUser subclass
user1 = BankUser("Bob", 1234, "password")
user2 = BankUser("Jim", 2468, "jimisbest123")
# Using deposit() method from BankUser subclass to deposit 5000 into user2's balance and printing both user1 and user2's balances
user2.deposit(5000)
print(user2.show_balance())
print(f"{user1.show_balance()}\n")

# If statements used to determine boolean value of transfer_money() and request_money() methods and printing necessary information

if user2.transfer_money(500, 2468):
    print("Transfer Authorized.")
    print("Transferring $500 to Bob")
    print(f"{user2.withdraw(500)}")
    print(f"{user1.deposit(500)}\n")

    if user1.request_money(250, 1234, "jimisbest123"):
        print("Request authorized.")
        print(f"{user1.name} sent $250")
        print(f"{user2.deposit(250)}")
        print(f"{user1.withdraw(250)}\n")
'''
