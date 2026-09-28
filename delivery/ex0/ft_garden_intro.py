#!/usr/bin/env python3
"""First python program, displaying a plant info"""


def ft_garden_intro() -> None:
    name: str = "dalia"
    height: int = 25
    age: int = 30

    print("=== Welcome to the Garden ===")
    print("Plant:", name.capitalize())
    print(f"Height: {height}cm")
    print("Age:", age, "days")
    print("=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
