def zodiac_sign(year):
    zodiacs = [
        "Rat (鼠 / Shǔ)",
        "Ox (牛 / Niú)",
        "Tiger (虎 / Hǔ)",
        "Rabbit (兔 / Tù)",
        "Dragon (龙 / Lóng)",
        "Snake (蛇 / Shé)",
        "Horse (马 / Mǎ)",
        "Goat (羊 / Yáng)",
        "Monkey (猴 / Hóu)",
        "Rooster (鸡 / Jī)",
        "Dog (狗 / Gǒu)",
        "Pig (猪 / Zhū)"
    ]

    i = (year - 1900) % 12
    return zodiacs[i]

def main():
    year = int(input("Enter your birth year that is greater than or equal to 1900: "))
    
    if year < 1900:
        print("Please enter a year greater than or equal to 1900.")
        return

    sign = zodiac_sign(year)
    print(f"Your Chinese zodiac sign is: {sign}")

main()
