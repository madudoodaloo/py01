#!/usr/bin/env python3

class Plant:
    """Base class representing a plant with nested statistics tracking."""

    class Stats:
        """Nested class tracking method call statistics."""

        def __init__(self) -> None:
            self._grow_count: int = 0
            self._age_count: int = 0
            self._show_count: int = 0

        def log_grow(self) -> None:
            self._grow_count += 1

        def log_age(self) -> None:
            self._age_count += 1

        def log_show(self) -> None:
            self._show_count += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_count} grow, "
                f"{self._age_count} age, {self._show_count} show"
            )

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self._height: float = float(height)
        self._age: int = int(age)
        self.stats: Plant.Stats = self.Stats()

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        """Static method checking if age exceeds 365 days."""
        return days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        """Class method factory for an unknown plant."""
        return cls("Unknown plant", 0.0, 0)

    def grow(self, cm: float = 0.8) -> None:
        self._height += cm
        self.stats.log_grow()

    def age(self, days: int = 1) -> None:
        self._age += days
        self.stats.log_age()

    def show(self) -> None:
        self.stats.log_show()
        print(
            f"{self.name.capitalize()}: {self._height:.1f}cm, "
            f"{self._age} days old"
        )


class Tree(Plant):
    """Specialized class for trees with extra shade statistics."""

    class Stats(Plant.Stats):
        """Extended nested stats class for trees."""

        def __init__(self) -> None:
            super().__init__()
            self._shade_count: int = 0

        def log_shade(self) -> None:
            self._shade_count += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade_count} shade")

    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: float = float(trunk_diameter)
        self.stats: Tree.Stats = self.Stats()

    def produce_shade(self) -> None:
        self.stats.log_shade()
        print(
            f"Tree {self.name.capitalize()} now produces a shade of "
            f"{round(self._height, 1)}cm long and "
            f"{round(self.trunk_diameter, 1)}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")


class Flower(Plant):
    """Specialized class for flowers."""

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self.is_blooming: bool = False

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.is_blooming:
            print(f"{self.name.capitalize()} is blooming beautifully!")
        else:
            print(f"{self.name.capitalize()} has not bloomed yet")


class Seed(Flower):
    """Specialized class inheriting from Flower, managing seed counts."""

    def __init__(
        self, name: str, height: float, age: int, color: str, seeds: int = 0
    ) -> None:
        super().__init__(name, height, age, color)
        self.seeds: int = seeds

    def bloom(self) -> None:
        super().bloom()
        if self.seeds == 0:
            self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


def show_plant_stats(plant: "Plant") -> None:
    """Standalone helper function to display plant statistics."""
    print(f"[statistics for {plant.name.capitalize()}]")
    plant.stats.display()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(
        f"Is 30 days more than a year? -> "
        f"{Plant.is_older_than_year(30)}"
    )
    print(
        f"Is 400 days more than a year? -> "
        f"{Plant.is_older_than_year(400)}\n"
    )

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    show_plant_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    show_plant_stats(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    show_plant_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    show_plant_stats(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    show_plant_stats(sunflower)

    print("\n=== Anonymous")
    anon = Plant.create_anonymous()
    anon.show()
    show_plant_stats(anon)


if __name__ == "__main__":
    main()
