#!/usr/bin/env python3
""" Plant Class and creating plant objects,
    with different attributes and display through instance methods"""


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name.capitalize()
        self.height: int = height
        self.age: int = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data() -> None:
    print("=== Garden Plant Registry ===")

    plant1 = Plant("rose", 25, 30)
    plant1.show()

    plant2 = Plant("Sunflower", 80, 45)
    plant2.show()

    plant3 = Plant("Cactus", 15, 120)
    plant3.show()


if __name__ == "__main__":
    ft_garden_data()
