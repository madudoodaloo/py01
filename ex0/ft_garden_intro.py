#!/usr/bin/env python3

def ft_garden_intro() -> None:
    name: str = "Dalia"
    height: int = 10
    age: int = 30

    print("=== Welcome to the Garden ===")
    print("Plant:", name)
    print(f"Height: {height}cm")
    print("Age:", age, "days")
    print("=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
