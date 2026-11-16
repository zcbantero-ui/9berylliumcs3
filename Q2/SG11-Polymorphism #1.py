# Zanti Carlos B. Antero
# 9 - Beryllium
# Nov/16-17/2026

class Patient:
  def __init__(self, name, ammount_bill):
    self.__name = name
    self.__ammount_bill = 0
    self.set_ammount_bill(ammount_bill)

  def get_name(self):
    return self.__name

  def get_ammount_bill(self):
    return self.__ammount_bill

  def set_name(self, name):
    self.__name = name

  def set_ammount_bill(self, ammount_bill):
    if ammount_bill < 0:
      print("Invalid ammount")
    else:
      self.__ammount_bill = ammount_bill

  def calculate_bill(self):
    return self.get_ammount_bill()

  def display_data(self):
    print(f"Patient Name: {self.get_name()}")
    print(f"Original Bill: {self.get_ammount_bill()}:,.2f")
    print(f"Patient Name: {self.calculate_bill()}:,.2f")
    print("")
    

class Senior_Patient(Patient):
  def calculate_bill(self):
    return self.get_ammount_bill() * (1 - 0.20)
    
class Philhealth_Patient(Patient):
  def calculate_bill(self):
    return self.get_ammount_bill() * (1 - 0.15)



regular_patient = Patient("Juan Dela Cruz", 15000)
senior_patient = Senior_Patient("Maria Santos", 15000)
philhealth_patient = Philhealth_Patient("Pedro Reyes", 15000)

print ("Hospital Billing System")
print ("----------------------------------------")

regular_patient.display_data()
senior_patient.display_data()
philhealth_patient.display_data()
