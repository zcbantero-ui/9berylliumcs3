#Zanti Carlos B. Antero 9-BERYLLIUM

class Bicycles:
    def __init__(self, bike_type, frame_metal, frame_brand, frame_color):
        self.type = bike_type
        self.frame_metal = frame_metal
        self.__frame_brand = frame_brand
        self.frame_color = frame_color

        self.frame = Frame(frame_metal, frame_brand, frame_color)

        self.bike_parts = []

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


class Frame:
    def __init__(self, metal, brand, color):
        self.metal = metal
        self.brand = brand
        self.color = color

    def __str__(self):
        return f"{self.color} {self.metal} frame ({self.brand})"


class ElectricBike(Bicycles):
    def __init__(self, bike_type, frame_metal, frame_brand, frame_color,
                 battery_capacity_wh, max_speed_kph):
        super().__init__(bike_type, frame_metal, frame_brand, frame_color)
        self.battery_capacity_wh = battery_capacity_wh
        self.max_speed_kph = max_speed_kph
        self.battery_level = 100

    def describe(self):
        base_description = super().describe()
        return (f"{base_description}, Battery: {self.battery_capacity_wh}Wh, "
                f"Max Speed: {self.max_speed_kph}kph")

    def drain_battery(self, percent):
        self.battery_level = max(0, self.battery_level - percent)
        print(f"{self.type} battery is now at {self.battery_level}%.")


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

    def tune_up(self, bicycle: Bicycles):
        print(f"{self.name} is tuning up the {bicycle.type} ({bicycle.frame})... done.")
