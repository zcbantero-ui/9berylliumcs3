# Zanti Carlos B. Antero
# 9 - Beryllium
# Nov/04/2026

class Animals: # set the parent class
    def __init__(self, name,): # initialize the attributes # Turns out, other than self, I only needed name as the attribute since im overriding eat, and make_sound in the child classes anyways welp.
        self.name = name
        self.Eat = eat
        self.Make_sound = make_sound
        
    def eat(self): # Eat function
        print("Eats")
    
    def make_sound(self): # Noise function
        print("Makes sounds")


class Lion(Animals): # Set child class for lion
    def __init__(self, name):
        super().__init__(name) 
    def eat(self): #Override
        print("eats fresh meat") #paste from given document
    def make_sound(self):
        print("roars loudly!")
        
class Elephant(Animals): # child class for elephant
    def __init__(self, name):
        super().__init__(name)
    def eat(self):
        print("eats grass and fruits") #paste from given document
    def make_sound(self):
        print("trumpets!")
      
class Ape(Animals): # child class for ape
    def __init__(self, name):
        super().__init__(name)
    def eat(self):
        print("eats bananas") #paste from given document
    def make_sound(self):
        print("chatters!")

#Sets the name od each animal
Lion = Lion("Simba")
Elephant = Elephant("Dumbo")
Ape = Ape("George")

#Output stuff, basically this part of the code SHOULD produce the required output.
print(f"{Lion.name()} {Lion.eat()}")
print(f"{Lion.name()} {Lion.make_sound()}")
print("----------------------")

print(f"{Elephant.name()} {Elephant.eat()}")
print(f"{Elephant.name()} {Elephant.make_sound()}")
print("----------------------")

print(f"{Ape.name()} {Ape.eat()}")
print(f"{Ape.name()} {Ape.make_sound()}")
print("----------------------")
