class Plant:

    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days

    def show(self):
        print(f"{self.name}: {round(self.height, 1):.1f}cm, {self.days} days old")

    def grow(self, rate_growth: float):
        self.height = round((self.height + rate_growth), 1)

    def age(self):
        self.days += 1


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    print("Created: ", end='')
    Plant("Rose", 25, 30).show()
    print("Created: ", end='')
    Plant("Oak", 200, 365).show()
    print("Created: ", end='')
    Plant("Cactus", 5, 90).show()
    print("Created: ", end='')
    Plant("Sunflower", 80, 45).show()
    print("Created: ", end='')
    Plant("Ferm", 15, 120).show()
