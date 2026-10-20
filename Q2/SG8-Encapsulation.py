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

Account1 = BankAccount("12345", 1000)

print("Account Number:", Account1.get_accountnumber)
print("Balance:", Account1.get_accountbalance)

print(Account1.get_acountbalance(-100))
