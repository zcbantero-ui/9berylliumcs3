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

        self.frame = Frame(frame_metal, frame_brand, frame_color)

    def get_frame_brand(self):
        return self.__frame_brand

    def describe(self):
        print(f"Type: {self.type}")
        print(f"Frame Metal: {self.frame_metal}")
        print(f"Frame Brand: {self.get_frame_brand()}")
        print(f"Frame Color: {self.frame_color}")

    def repaint(self, new_color):
        self.frame_color = new_color
        self.frame.color = new_color
        print(f"{self.type} has been repainted to {new_color}.")


class ElectricBike(Bicycles):
    def __init__(self, bike_type, frame_metal, frame_brand, frame_color, battery):
        super().__init__(bike_type, frame_metal, frame_brand, frame_color)
        self.battery = battery

    def describe(self):
        super().describe()
        print(f"Battery: {self.battery} Wh")


class BikeParts:
    def __init__(self, part_type, color, quantity):
        self.part_type = part_type
        self.color = color
        self.quantity = quantity

    def purchase(self, amount):
        self.quantity += amount
        print(f"Purchased {amount} {self.part_type}(s).")
        print(f"New quantity: {self.quantity}")


# MECHANIC CLASS
class Mechanic:
    def __init__(self, name):
        self.name = name

    def tune_up(self, bicycle):
        print(f"{self.name} is tuning up the {bicycle.type}.")

print("=== TEST 1: INHERITANCE ===")

ebike = ElectricBike(
    "Electric Bike",
    "Aluminum",
    "Giant",
    "Blue",
    500
)

ebike.describe()


print()
print("=== TEST 2: COMPOSITION ===")

bike = Bicycles(
    "Mountain Bike",
    "Aluminum",
    "Trek",
    "Black"
)

print(f"Bike: {bike.type}")
print(f"Frame: {bike.frame}")


print()
print("=== EXTRA TEST: INHERITED METHOD ===")

bike.repaint("Red")

print(f"Updated frame: {bike.frame}")
