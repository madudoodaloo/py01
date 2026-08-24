#!/usr/bin/env pyhton3

class Plant:
	def __init__(self, name: str, height: int, age: int) -> None:
		self.name: str = name
		self.height: int = height
		self.age: int = age

	def show(self) -> None:
		print(f"{self.name}: {self.height}cm, {self.age} days old")

def ft_garden_data() -> None:
	print("=== Garden Plant Registry ===")

	# Instantiating Plant 1
	plant1 = Plant("Rose", 25, 30)
	plant1.show()

	# Instantiating Plant 2
	plant2 = Plant("Sunflower", 80, 45)
	plant2.show()

	# Instantiating Plant 3
	plant3 = Plant("Cactus", 15, 120)
	plant3.show()

if __name__ == "__main__":
	ft_garden_data()
