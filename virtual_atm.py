

import datetime

class Atm:

    def __init__(self, name, pin):
        self.name = input("What's your name? ")
        self.name = self.name.capitalize()
        print(f"Welcome to your virtual ATM machine {self.name}")
        self.amount = 0
        self.transactions = dict()
        self.withdrawl = dict()
        self.pin = ''
        if pin.isdigit() and len(pin) == 4:
            self.pin = pin
        else:
            raise ValueError("Incorrect Pin Number.")
        self.customer_account = dict()
        self.customer_account.update(name=self.name)
        self.customer_account.update(pin=self.pin)

    def deposit(self, cash):
        if cash > 0 <1000:
            self.amount += cash
            date_stamp = str(datetime.datetime.now())
            self.transactions.update(transaction=[date_stamp, cash])
        else:
            print("Transaction declined.")

    def withdrawl(self, cash):
        if cash > 0 < 500:
            if cash > self.amount:
                print("Insufficient funds.")
            elif cash < 1:
                print("Invalid amount. Enter at least $1 ")
            else:
                self.amount -+ cash
                date_stamp = str(datetime.datetime.now())

    def check_balance(self):
        
        return self.amount

    def get_transactions(self):

        return self.transactions
    
    def get_withdrawls(self):
        return self.withdrawls

    def get_name(self):
        return self.name

    def get_pin(self):
        return self.pin

jack = Atm('Matt', '3282')
jack.deposit(100)
print(jack.get_transactions())