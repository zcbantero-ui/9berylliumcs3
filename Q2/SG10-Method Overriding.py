# Zanti Carlos B. Antero
# 9 - Beryllium
# Nov/04/2026

class Animals:
    def __init__(self, eat, make_sound):
        self.Eat = eat
        self.Make_sound = make_sound
        self.name = name
        
    def eat(self):
        print(f"{self.name} chows on {self.Eat}")
    
    def make_sound(self):
        print(f"{self.name} {self.Make_sound}")


class Lion(Animals):
    def __init__(self, name):
        super().__init__("T-bone steak", "ROAAR", name)

class Elephant(Animals):
    def __init__(self, name):
        super().__init__("Peanuts", "TOOOT", name)

class Ape(Animals):
    def __init__(self, name):
        super().__init__("Bananas", "OOO OOO, AAA AAA", name)


Lion = Lion("Simba")
Elephant = Elephant("Dumbo")
Ape = Ape("George")

Lion.make_sound
Lion.eat
print("----------------------")

Elephant.make_sound
Elephant.eat
print("----------------------")

Ape.make_sound
Ape.eat
print("----------------------")
