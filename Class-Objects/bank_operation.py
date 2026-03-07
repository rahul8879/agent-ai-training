class BankAccount:
    def __init__(self,account_number,account_holder,intial_balance=0.0,account_type="Savings"):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = intial_balance # __ for private variable and _ for protected variable
        self.account_type = account_type
    def deposit(self,amount):
        if amount>0:
            self.__balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self,amount):
        if amount>0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance amount.")

    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: ${self.__balance:.2f}")



class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, initial_balance=0.0, interest_rate=0.04, minimum_balance=0.0):
        super().__init__(account_number, account_holder, initial_balance, account_type="Savings")
        self.interest_rate = interest_rate
        self.__minimum_balance = minimum_balance

    def apply_interest(self):
        interest_amount = self.get_balance() * self.interest_rate
        self.set_balance(self.get_balance() + interest_amount)
        print(f"Interest applied: ${interest_amount:.2f}")

    # overide the withdraw function
    def withdraw(self, amount):
        if amount > 0:
            if self.get_balance() - amount >= self.__minimum_balance:
                self.set_balance(self.get_balance() - amount)
                print(f"Withdrew ${amount:.2f}. New balance: ${self.get_balance():.2f}")
            else:
                print("Cannot withdraw. Minimum balance requirement not met.")
        else:
            print("Invalid withdrawal amount.")

    def display_account_info(self):
        super().display_account_info()
        print(f"Interest Rate: {self.interest_rate * 100:.2f}%")
        print(f"Minimum Balance: ${self.__minimum_balance:.2f}")
