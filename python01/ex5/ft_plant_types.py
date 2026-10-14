class Plant:

    def __init__(self, name, height, age):
        self.name = name
        self._height = height or 0
        self._age = age or 0

    def show(self):
        print(f"{self.name}: {round(self.get_height()):.1f}cm, {self.get_age()} days old")

    def grow(self, rate_growth: float):
        self.height = round((self.get_height() + rate_growth), 1)

    def age(self):
        self.set_age(self.get_age() + 1)
    
    def get_age(self):
        return self._age
    
    def get_height(self):
        return self._height
    
    def set_age(self, new_age):
        if(new_age < 0):
            return
        else:
            self._days = new_age
            return
        
    def set_height(self, new_height):
        if(new_height < 0):
            return
        else:
            self._height = new_height


class   Three(Plant):

    def __init__(self, name, height, age,  trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.is_shade = False

    def show(self):
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")
        if self.is_shade:
            print(f"Tree {self.name} now produces a shade of {round(self.get_height(), 1)}cm long and {round(self.trunk_diameter, 1)}cm wide.")

    def produce_shade(self):
        self.is_shade = True

class   Flower(Plant):

    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.is_blommed = False

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.is_blommed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")

    def bloom(self):
        self.is_blommed = True


class Vegetable(Plant):

    def __init__(self, name, height, age,  harvest_season,  nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def age(self):
        super().age()
        self.nutritional_value += 1
    

if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    f = Flower("Rose", 15, 10, "red")
    f.show()
    print("[asking the rose to bloom]")
    f.bloom()
    f.show()
    print("=== Three")
    t = Three("Oak", 200, 365, 5)
    t.show()
    print("[asking the oak to produce shade]")
    t.produce_shade()
    t.show()
    print("=== Vegetable")
    v = Vegetable("tomato", 5, 10, "April", 0)
    v.show()
    for x in range(1, 20):
        v.grow(0.8)
        v.age()
    v.show()