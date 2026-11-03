# Zanti Carlos B. Antero
# 9 - Beryllium
# Nov/04/2026

class Animals: # set the parent class
    def __init__(self, eat, make_sound): # initialize the attributes
        self.name = name
        self.Eat = eat
        self.Make_sound = make_sound
        
    def eat(self): # Eat function
        print(f"{self.name} chows on {self.Eat}")
    
    def make_sound(self): # Noise function
        print(f"{self.name} {self.Make_sound}")


class Lion(Animals): # Set child class for lion
    def __init__(self, name):
        super().__init__(name, "fresh meat", "roars loudly!") 

class Elephant(Animals): # child class for elephant
    def __init__(self, name):
        super().__init__(name, "grass and fruits", "trumpets!")

class Ape(Animals): # child class for ape
    def __init__(self, name):
        super().__init__(name, "bananas", "chatters!")


Lion = Lion("Simba")
Elephant = Elephant("Dumbo")
Ape = Ape("George")

print (f"{Lion.name} eats {Lion.eat}")
print (f"{Lion.name}  {Lion.make_sound}")
print("----------------------")

print (f"{Elephant.name} eats {Elephant.eat}")
print (f"{Elephant.name}  {Elephant.make_sound}")
print("----------------------")

print (f"{Ape.name} eats {Ape.eat}")
print (f"{Ape.name}  {Ape.make_sound}")
print("----------------------")
