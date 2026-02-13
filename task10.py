class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Hisob toldirildi. Yangi balans: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Pul yechildi. Yangi balans: {self.balance}")
        else:
            print("Xatolik: Hisobda yetarli mablag yoq!")
