#Zanti Carlos B. Antero 9-BERYLLIUM

class Bicycles:
    def __init__(self, bike_type, frame_metal, frame_brand, frame_color):
        self.type = bike_type
        self.frame_metal = frame_metal
        self.__frame_brand = frame_brand 
        self.frame_color = frame_color

        self.bike_parts = []

    def repaint(self, new_color):
        self.frame_color = new_color
        print(f"{self.type} has been repainted to {self.frame_color}.")

    def get_frame_brand(self):
        return self.__frame_brand

    def describe(self):
        return (f"Type: {self.type}, Frame Metal: {self.frame_metal}, "
                f"Brand: {self.get_frame_brand()}, Color: {self.frame_color}")

    def add_part(self, part_reference):
        """Stores an actual BikeParts object reference inside this bike."""
        self.bike_parts.append(part_reference)
        print(f"Added '{part_reference.part_type}' to {self.type}.")

    def list_parts(self):
        print(f"Parts installed on {self.type} ({self.get_frame_brand()}):")
        for part in self.bike_parts:
            print(f"  - {part.part_type} | color: {part.color} | quantity: {part.quantity}")


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


object1 = Bicycles("MountainBike", "Carbon", "Giant", "Blue")
object2 = Bicycles("RoadBike", "AluminumAlloy", "Classic", "Red")

print("--- BEFORE ---")
print("Object 1:", object1.describe())
print("Object 2:", object2.describe())

print("\nPerforming action on Object 1 (repaint to Black)...")
object1.repaint("Black")

print("\n--- AFTER ---")
print("Object 1:", object1.describe())
print("Object 2:", object2.describe())


print("\n\n--- BEFORE RELATIONSHIP ---")

part1 = BikeParts("Wheel", "Black", 2)
part2 = BikeParts("Gear Set", "Silver", 1)
part3 = BikeParts("Brake Pads", "Red", 4)

print(f"Created part: {part1.part_type}, qty {part1.quantity}")
print(f"Created part: {part2.part_type}, qty {part2.quantity}")
print(f"Created part: {part3.part_type}, qty {part3.quantity}")
print(f"\nDoes {object1.type} have any parts yet? {len(object1.bike_parts)} part(s) attached.")

print("\n--- BUILDING RELATIONSHIP ---")

object1.add_part(part1)
object1.add_part(part2)
object1.add_part(part3)

print("\n--- AFTER RELATIONSHIP ---")

object1.list_parts()

print(f"\nTotal parts now attached to {object1.type}: {len(object1.bike_parts)}")
