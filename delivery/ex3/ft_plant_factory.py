#!/usr/bin/env python3
"""Streamlining the plant creation process:
instantiate and initialize a class"""


class Plant:
    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age_days: int = age_days

    def show(self) -> None:
        print(
            f"{self.name}: {round(self.height, 1)}cm, "
            f"{self.age_days} days old")

    def grow(self, cm: float = 0.8) -> None:
        self.height += cm

    def age(self, grow_days: int = 1) -> None:
        self.age_days += grow_days


def ft_plant_growth() -> None:
    print("=== Plant Factory Output ===")
    plants: list[Plant] = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120),
        Plant("Dalia", 50.0, 1),
    ]
    for plant in plants:
        print("Created: ", end="")
        plant.show()

    print()
    print("=== Testing age() and grow() methods ===")
    plant = plants[0]
    for day in range(1, 8):
        plant.grow(day)
        plant.age(1)
        print(f"=== Day {day} ===")
        plant.show()


if __name__ == "__main__":
    ft_plant_growth()
