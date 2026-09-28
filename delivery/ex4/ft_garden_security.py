#!/usr/bin/env python3
"""Protected attributes using explicit encapsulation."""


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self._height: float = 0.0
        self._age: int = 0
        self._is_initialized: bool = False

        self.set_height(height)
        self.set_age(age)
        self._is_initialized = True
        self.show("Plant created")

    # Accessors (Getters)
    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    # Mutators (Setters)
    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            if self._is_initialized:
                print("Height update rejected")
        else:
            self._height = float(height)
            if self._is_initialized:
                print(f"Height updated: {int(self._height)}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            if self._is_initialized:
                print("Age update rejected")
        else:
            self._age = int(age)
            if self._is_initialized:
                print(f"Age updated: {self._age} days")

    def grow(self, cm: float = 0.8) -> None:
        self.set_height(self._height + cm)

    def age(self, grow_days: int = 1) -> None:
        self.set_age(self._age + grow_days)

    def show(self, prefix: str = "Current state") -> None:
        print(
            f"{prefix}: {self.name}: {self._height:.1f}cm, "
            f"{self._age} days old"
        )


def ft_garden_security() -> None:
    print("=== Garden Security System ===")

    plant = Plant("Rose", 15.0, 10)

    print()
    plant.set_height(25.0)
    plant.set_age(10)

    print()
    plant.show()

    print()
    print("==== Testing invalid input in setters")
    plant.set_height(-5.0)
    plant.set_age(-10)
    plant.show()

    print()
    print("==== Testing invalid input in methods")
    plant.grow(-30)
    plant.age(-20)
    plant.show()


if __name__ == "__main__":
    ft_garden_security()
