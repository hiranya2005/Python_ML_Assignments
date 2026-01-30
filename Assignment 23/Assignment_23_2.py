class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account Holder Name:", self.Name)
        print("Current Balance:", self.Amount)

    def Deposit(self):
        deposit_amount = float(input("Enter amount to deposit: "))
        self.Amount += deposit_amount
        print("Amount deposited successfully.")

    def Withdraw(self):
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount <= self.Amount:
            self.Amount -= withdraw_amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance. Withdrawal not allowed.")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest

Obj1 = BankAccount("Ramesh", 50000)
Obj2 = BankAccount("Suresh", 30000)

print("\n--- Account 1 Details ---")
Obj1.Display()
Obj1.Deposit()
Obj1.Withdraw()
print("Interest:", Obj1.CalculateInterest())
Obj1.Display()

print("\n--- Account 2 Details ---")
Obj2.Display()
Obj2.Deposit()
Obj2.Withdraw()
print("Interest:", Obj2.CalculateInterest())
Obj2.Display()