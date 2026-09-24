# Zanti Carlos B. Antero 9-BERYLLIUM

class Frame:
    def __init__(self, metal, brand, color):
        self.metal = metal
        self.brand = brand
        self.color = color

    def __str__(self):
        return f"{self.color} {self.metal} frame ({self.brand})"


class Bicycles:
    def __init__(self, bike_type, frame_metal, frame_brand, frame_color):
        self.type = bike_type
        self.frame_metal = frame_metal
        self.__frame_brand = frame_brand
        self.frame_color = frame_color
        self.bike_parts = []
        self.frame = Frame(frame_metal, frame_brand, frame_color)

    def repaint(self, new_color):
        self.frame_color = new_color
        self.frame.color = new_color
        print(f"{self.type} has been repainted to {self.frame_color}.")

    def get_frame_brand(self):
        return self.__frame_brand

    def describe(self):
        return (f"Type: {self.type}, Frame Metal: {self.frame_metal}, "
                f"Brand: {self.get_frame_brand()}, Color: {self.frame_color}")

    def add_part(self, part_reference):
        self.bike_parts.append(part_reference)
        print(f"Added '{part_reference.part_type}' to {self.type}.")

    def list_parts(self):
        print(f"Parts installed on {self.type} ({self.get_frame_brand()}):")
        for part in self.bike_parts:
            print(f"  - {part.part_type} | color: {part.color} | quantity: {part.quantity}")


class ElectricBike(Bicycles):
    def __init__(self, bike_type, frame_metal, frame_brand, frame_color, battery):
        super().__init__(bike_type, frame_metal, frame_brand, frame_color)
        self.battery = battery

    def describe(self):
        return (f"{super().describe()}, Battery: {self.battery} Wh")


class BikeParts:
    def __init__(self, part_type, color, quantity):
        self.part_type = part_type
        self.color = color
        self.quantity = quantity

    def install(self, quantity):
        print(f"Installing {quantity} unit(s) of {self.part_type}.")

    def remove(self, quantity):
        print(f"Removing {quantity} unit(s) of {self.part_type}.")

    def purchase(self, quantity):
        self.quantity += quantity
        print(f"Purchased {quantity} more {self.part_type}(s). New quantity: {self.quantity}")

    def sell(self):
        print(f"{self.part_type} has been sold.")


class Mechanic:
    def __init__(self, name):
        self.name = name

    def tune_up(self, bicycle):
        print(f"{self.name} is tuning up the {bicycle.type}.")


object1 = Bicycles("MountainBike", "Carbon", "Giant", "Blue")
object2 = Bicycles("RoadBike", "AluminumAlloy", "Classic", "Red")

print("--- BEFORE ---")
print("Object 1:", object1.describe())
print("Object 2:", object2.describe())

print("\nPerforming action on Object 1 (repaint to Black)...")
object1.repaint("Black")

print("\n========================================")
print("STEP 10 - ADVANCED RELATIONSHIP TESTS")
print("========================================")

print("\n--- TEST 1: INHERITANCE ---")

electric1 = ElectricBike(
    "ElectricBike",
    "Carbon",
    "Giant",
    "Blue",
    500
)

print(electric1.describe())

print("\nElectricBike inherited the following from Bicycles:")
print("Type:", electric1.type)
print("Frame Metal:", electric1.frame_metal)
print("Frame Brand:", electric1.get_frame_brand())
print("Frame Color:", electric1.frame_color)

print("\n--- TEST 2: COMPOSITION ---")

bike1 = Bicycles(
    "MountainBike",
    "Carbon",
    "Giant",
    "Blue"
)

print("Bike:", bike1.type)
print("Frame:", bike1.frame)

print("\nThe Bicycles object contains a Frame object.")
print("This demonstrates a HAS-A Composition relationship.")

print("\n--- EXISTING BIKE PARTS TEST ---")

pedal = BikeParts("Pedal", "Black", 2)

bike1.add_part(pedal)
bike1.list_parts()

print("\nBike parts can also be purchased:")
pedal.purchase(2)

print("\n--- MECHANIC TEST ---")

mechanic1 = Mechanic("Carlos")
mechanic1.tune_up(bike1)
