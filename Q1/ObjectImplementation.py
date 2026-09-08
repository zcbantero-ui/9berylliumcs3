#Zanti Carlos B. Antero 9-BERYLLIUM

class Bicycles:
    def __init__(self, bike_type, frame_metal, frame_brand, frame_color):
        self.type = bike_type
        self.frame_metal = frame_metal
        self.__frame_brand = frame_brand  # private attribute
        self.frame_color = frame_color

    def repaint(self, new_color):
        self.frame_color = new_color
        print(f"{self.type} has been repainted to {self.frame_color}.")

    def get_frame_brand(self):
        return self.__frame_brand

    def describe(self):
        return (f"Type: {self.type}, Frame Metal: {self.frame_metal}, "
                f"Brand: {self.get_frame_brand()}, Color: {self.frame_color}")


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
