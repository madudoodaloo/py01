#!/usr/bin/env python3

class Plant:
	def __init__(self, name: str, height: float, age_days: int) -> None:
		self.name: str = name
		self.height: float = height
		self.age_days: int = age_days
		print(f"Created: {self.name}: {round(self.height, 1)}cm, {self.age_days} days old")

	def show(self) -> None:
		print(f"{self.name}: {round(self.height, 1)}cm, {self.age_days} days old")

	
	
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
	plants[5].show()

if __name__ == "__main__":
	ft_plant_growth()
