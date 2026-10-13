# Zanti Carlos B. Antero
# 9 - Beryllium
# Oct/13/2026

class BankAccount:
    def __init__(self, accountnumber, accountbalance):
        self.__accountnumber = accountnumber
        self.__accountbalance = accountbalance
    
    def set_accountnumber(self, accountnumber): 
        self.__accountnumber = accountnumber
    
    def set_accountbalance(self, newaccountbalance):
        print(f"Update balance to {newaccountbalance}")
        if newaccountbalance < 0:
            print("Balance cannot be negative. Balance not updated.")
        else:
            self.__accountbalance = newaccountbalance

    @property 
    def get_accountnumber(self):
        return self.__accountnumber

    @property
    def get_accountbalance(self):
        return self.__accountbalance

a1 = BankAccount("12345", 1000)

print("Account Number:", a1.get_accountnumber)
print("Balance:", a1.get_accountbalance)

print(a1.set_acountbalance(-100))
