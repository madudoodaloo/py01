#!/usr/bin/env python3 

class Plant:
	"""Class representing a protected plant using explicit encapsulation."""
	def __init__(self, name: str, height: float, age: int):
		self.name: str = name
		self._height: float = 0.0
		self._age: int = 0

		if self.set_height(height) < 0:
			return 
		elif self.set_age(age) < 0:
			return 
		else:
			print(f"Created: {self.name}: {round(self._height, 1)}cm, {self._age} days old")
		
	# Accessors (Getters)
	def get_height(self) -> float:
		return self._height
	
	def get_age(self) -> int:
		return self._age

	# Mutators (Setters)
	def set_height(self, height: float) -> int:
		if height < 0:
			print(f"{self.name}: Error, height can't be negative")
			if self._height > 0:
				print("Height update rejected")
			return -1
		else:
			if self._height > 0:
				print(f"Height updated: {int(self._height)}cm")
			self._height = float(height)
			return 0

	def set_age(self, age: int) -> None:
		if age < 0:
			print(f"{self.name}: Error, age can't be negative")
			if self._age > 0:
				print("Age update rejected")
			return -1
		else:
			if self._age > 0:
				print(f"Age updated: {self._age} days")
			self._age = int(age)
			return 0

	def show(self) -> None:
		print(f"Current state: {self.name}: {self._height:.1f}cm, {self._age} days old")

def ft_garden_security() -> None:
	print("=== Garden Security System ===")
	
	plant = Plant("Rose", 15.0, 20)
	plant.set_height(25.0)
	plant.set_age(2)

	plant.set_height(9)
	plant.set_height(-9)
	plant.set_age(-20)

	plant.show()

if __name__ == "__main__":
	ft_garden_security()