class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} hisobiga {amount} qoshildi.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} hisobidan {amount} yechildi.")
        else:
            print(f"{self.owner} hisobida mablag yetarli emas!")

    def show_balance(self):
        print(f"{self.owner} balansi: {self.balance}")

acc1 = BankAccount("Ali", 1000)
acc2 = BankAccount("Vali", 500)
acc3 = BankAccount("Hasan", 2000)
