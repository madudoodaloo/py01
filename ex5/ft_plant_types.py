#!/usr/bin/env python3


class Plant:
    """Class representing a protected plant using explicit encapsulation."""

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self._height: float = 0.0
        self._age: int = 0
        self._is_initialized: bool = False

        self.set_height(height)
        self.set_age(age)

        self._is_initialized = True

    # Accessors (Getters)
    def get_height(self) -> float:
        """Safely return plant height."""
        return self._height

    def get_age(self) -> int:
        """Safely return plant age."""
        return self._age

    # Mutators (Setters)
    def set_height(self, height: float) -> None:
        """Sets plant height with input validation."""
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            if self._is_initialized:
                print("Height update rejected")
        else:
            self._height = float(height)
            if self._is_initialized:
                print(f"Height updated: {int(self._height)}cm")

    def set_age(self, age: int) -> None:
        """Sets plant age with input validation."""
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            if self._is_initialized:
                print("Age update rejected")
        else:
            self._age = int(age)
            if self._is_initialized:
                print(f"Age updated: {self._age} days")

    def grow(self, cm: float = 0.8) -> None:
        self._height += cm

    def age(self, grow_days: int = 1) -> None:
        self._age += grow_days

    def show(self) -> None:
        """Display current plant info."""
        print(
            f"{self.name}: {self._height:.1f}cm, "
            f"{self._age} days old"
        )


class Flower(Plant):
    """Specialized class for flowers"""

    def __init__(
            self, name: str, height: float, age: int, color: str) -> None:
        print("=== Flower")
        super().__init__(name, height, age)
        self.color: str = color
        self.is_blooming: bool = False

    def bloom(self) -> None:
        """Sets Flower to Bloom"""
        print(f"[asking the {self.name} to bloom]")
        self.is_blooming = True

    def show(self) -> None:
        """Override show() to display flower(plant) info"""
        super().show()
        print(f"Color: {self.color}")
        if self.is_blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    """Specialized class for Trees"""

    def __init__(
            self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        print("=== Tree")
        super().__init__(name, height, age)
        self.trunk_diameter: float = float(trunk_diameter)

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(
            f"Tree {self.name} now produces a shade of "
            f"{round(self._height, 1)}cm long and "
            f"{round(self.trunk_diameter, 1)}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")


class Vegetable(Plant):
    """Specialized class for Vegetables"""

    def __init__(
            self, name: str, height: float, age: int, harvest_season: str
    ) -> None:
        print("=== Vegetable")
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = 0

    def grow(self, growth_cm: float) -> None:
        print(f"[make {self.name} grow {round(growth_cm, 1)}cm]")
        self.nutritional_value += growth_cm / 2
        super().grow(growth_cm)

    def age(self, days_older: int) -> None:
        print(f"[make {self.name} grow {days_older} days older]")
        self.nutritional_value += days_older
        super().age(days_older)

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season.capitalize()}")
        print(f"Nutritional value: {self.nutritional_value}")


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")

    flower = Flower("Dalia", 15.0, 10, "pink")
    print("=== show ===")
    flower.show()
    flower.bloom()
    flower.show()

    tree = Tree("Carvalho", 200, 365, 5)
    print("=== show ===")
    tree.show()
    tree.produce_shade()

    vege = Vegetable("Tomate", 5, 10, "April")
    print("=== show ===")
    vege.show()
    vege.grow(5)
    vege.show()
    vege.age(20)
    vege.show()


if __name__ == "__main__":
    ft_plant_types()