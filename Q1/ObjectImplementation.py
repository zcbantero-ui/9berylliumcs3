#Zanti Carlos B. Antero 9-BERYLLIUM

class Bicycles:
    def __init__(self, bike_type, frame_metal, frame_brand, frame_color):
        self.type = bike_type
        self.frame_metal = frame_metal
        self.__frame_brand = frame_brand  # private
        self.frame_color = frame_color

    def repaint(self, new_color):
        self.frame_color = new_color

    def get_frame_brand(self):
        return self.__frame_brand

    def describe(self):
        return f"{self.type} | {self.frame_metal} | {self.get_frame_brand()} | {self.frame_color}"


def make_bike(label):
    print(f"\n{label}:")
    return Bicycles(
        input("  Type: "), input("  Frame metal: "),
        input("  Frame brand: "), input("  Frame color: ")
    )


b1 = make_bike("Object 1")
b2 = make_bike("Object 2")

while True:
    choice = input("\n[1] Repaint b1  [2] Repaint b2  [3] Show both  [4] Quit: ")
    if choice == "1":
        b1.repaint(input("New color: "))
    elif choice == "2":
        b2.repaint(input("New color: "))
    elif choice == "3":
        print("b1:", b1.describe())
        print("b2:", b2.describe())
    elif choice == "4":
        print("b1:", b1.describe())
        print("b2:", b2.describe())
        break
