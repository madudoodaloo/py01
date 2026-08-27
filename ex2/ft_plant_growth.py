#!/usr/bin/env python3

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
    print("=== Garden Plant Growth ===")
    plant = Plant("Dalia", 25.0, 30)
    plant.show()

    initial_height: float = plant.height

    for day in range(1, 8):
        plant.grow()
        plant.age(1)
        print(f"=== Day {day} ===")
        plant.show()

    weekly_growth: float = plant.height - initial_height
    print(f"Growth this week: {round(weekly_growth, 2)}cm")


if __name__ == "__main__":
    ft_plant_growth()
