class Plant:

    def __init__(self, name, height, days):
        self.name = name
        self._height = height or 0
        self._days = days or 0

    def show(self):
        print(f"{self.name}: {round(self.get_height()):.1f}cm, {self.get_age()} days old")

    def grow(self, rate_growth: float):
        self.height = round((self.get_height() + rate_growth), 1)

    def age(self):
        self.set_age(self.get_age() + 1)
    
    def get_age(self):
        return self._days
    
    def get_height(self):
        return self._height
    
    def set_age(self, new_age):
        if(new_age < 0):
            return print(f"{self.name}: Error, age can't be negative \nAge update rejected")
        else:
            self._days = new_age
            return print(f"Age updated: {self.get_age()} days\n")
        
    def set_height(self, new_height):
        if(new_height < 0):
            return print(f"{self.name}: Error, height can't be negative \nHeight update rejected")
        else:
            self._height = new_height
            return print(f"\nHeight updated: {self.get_height()}cm")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    p1 = Plant("Rose", 15, 10)
    print(f"Plant created: ", end='')
    p1.show()
    p1.set_height(25)
    p1.set_age(30)
    p1.set_height(-10)
    p1.set_age(-10)
    print("\nCurrent State: ", end='')
    p1.show()