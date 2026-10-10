class Plant:
    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days
    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.days} days old")
    def grow(self, rate_growth : float):
        self.height = round((self.height + rate_growth), 1)
    def age(self):
         self.days += 1
if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    p1 = Plant("Rose", 25, 30)
    for p in range(0,8):
        p1.show()
        p1.grow(0.8)
        p1.age()
        if (p < 7):
            print(f"=== Day {p + 1} ===")
    print(f"Growth this week: {round(p * 0.8, 1)}cm")