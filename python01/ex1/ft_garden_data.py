class Plant:
    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days
    def show(self):
        print(f"{self.name}: {self.height}cm {self.days} days old")
        
if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    Plant("Rose", 25, 30).show()
    Plant("Sunflower", 80, 45).show()
    Plant("Cactus", 15, 120).show()