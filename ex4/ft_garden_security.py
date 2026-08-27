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
        print(
            f"Plant created: {self.name}: {self._height:.1f}cm, "
            f"{self._age} days old"
        )

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

    def show(self) -> None:
        """Display current plant info."""
        print(
            f"Current state: {self.name}: {self._height:.1f}cm, "
            f"{self._age} days old"
        )


def ft_garden_security() -> None:
    print("=== Garden Security System ===")

    plant = Plant("Rose", 15.0, 10)
    plant.set_height(25.0)
    plant.set_age(30)

    plant.set_height(-5.0)
    plant.set_age(-10)

    plant.show()


if __name__ == "__main__":
    ft_garden_security()
