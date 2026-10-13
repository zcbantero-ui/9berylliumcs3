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
        if newbalance < 0:
            print("Balance cannot be negative. Balance not updated.")
        else:
            self.__balance = newaccountbalance
    
    def get_accountnumber(self):
        return self.__accountnumber
        pin = "password123"
        enterPin = input("Enter your pin: ")
        if enterPassword == password:
            return self.__accountnumber
        else:
            print("Wrong pin, access denied.")
            return None

    def get_balance(self):
        return self.__balance
