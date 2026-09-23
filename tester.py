#!/usr/bin/env python3

"""
Helper file for Code Cultivation - Module 01: Object-Oriented Garden Systems.

This file allows you to test all exercises from the parent directory.
Run: python3 main.py

Expected directory structure:
.
├── main.py
├── ex0/
│   └── ft_garden_intro.py
├── ex1/
│   └── ft_garden_data.py
├── ex2/
│   └── ft_plant_growth.py
├── ex3/
│   └── ft_plant_factory.py
├── ex4/
│   └── ft_garden_security.py
├── ex5/
│   └── ft_plant_types.py
└── ex6/
    └── ft_garden_analytics.py
"""

import os
import sys
import runpy
import importlib.util

EXERCISES = {
    "0": ("ex0", "ft_garden_intro", "Planting Your First Seed"),
    "1": ("ex1", "ft_garden_data", "Garden Data Organizer"),
    "2": ("ex2", "ft_plant_growth", "Plant Growth Simulator"),
    "3": ("ex3", "ft_plant_factory", "Plant Factory"),
    "4": ("ex4", "ft_garden_security", "Garden Security System"),
    "5": ("ex5", "ft_plant_types", "Specialized Plant Types"),
    "6": ("ex6", "ft_garden_analytics", "Garden Analytics"),
}


def check_exercise_requirements(folder_name: str, module) -> None:
    """Inspect loaded module against Module 01 OOP subject requirements."""
    if folder_name == "ex1":
        if not hasattr(module, "Plant"):
            print("⚠️ Warning: Exercise 1 expects a 'Plant' class.")
        elif not hasattr(getattr(module, "Plant"), "show"):
            print("⚠️ Warning: 'Plant' class should have a 'show()' method.")

    elif folder_name == "ex2":
        plant_cls = getattr(module, "Plant", None)
        if plant_cls:
            if not hasattr(plant_cls, "grow") or not hasattr(plant_cls, "age"):
                print("⚠️ Warning: 'Plant' class needs 'grow()' and 'age()' methods.")

    elif folder_name == "ex4":
        plant_cls = getattr(module, "Plant", None)
        if plant_cls:
            expected = ["get_height", "set_height", "get_age", "set_age"]
            missing = [m for m in expected if not hasattr(plant_cls, m)]
            if missing:
                print(f"⚠️ Warning: 'Plant' missing method(s): {', '.join(missing)}")

    elif folder_name == "ex5":
        expected_classes = ["Flower", "Tree", "Vegetable"]
        missing = [c for c in expected_classes if not hasattr(module, c)]
        if missing:
            print(f"⚠️ Warning: Missing specialized class(es): {', '.join(missing)}")

    elif folder_name == "ex6":
        if not hasattr(module, "Seed"):
            print("⚠️ Warning: Exercise 6 expects a 'Seed' class.")


def test_ft_exercise(folder_name: str, exercise_file_name: str, title: str) -> None:
    """Run and test an exercise from its respective subfolder."""
    print(f"\n=== Testing {folder_name}/{exercise_file_name}.py ({title}) ===")

    file_path = os.path.join(folder_name, f"{exercise_file_name}.py")

    if not os.path.exists(file_path):
        print(f"❌ Could not find {file_path}")
        print(f"   Ensure directory '{folder_name}' and file '{exercise_file_name}.py' exist.")
        return

    abs_folder = os.path.abspath(folder_name)
    path_added = False
    if abs_folder not in sys.path:
        sys.path.insert(0, abs_folder)
        path_added = True

    try:
        spec = importlib.util.spec_from_file_location(exercise_file_name, file_path)
        if spec is None or spec.loader is None:
            raise ImportError(f"Failed to load spec for {file_path}")

        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        check_exercise_requirements(folder_name, module)

        print(f"--- Running {exercise_file_name}.py ---\n")
        runpy.run_path(file_path, run_name="__main__")

    except ImportError as error:
        print(f"❌ Import error: {error}")
        print("   Check your imports in the exercise file.")

    except AttributeError as error:
        print(f"❌ Attribute error: {error}")
        print("   Check class, method, or attribute names against subject requirements.")

    except TypeError as error:
        print(f"❌ Type error: {error}")
        print("   Check method signatures and argument types.")

    except Exception as error:
        print(f"❌ Error running your code: {error}")
        print("   Check your code for syntax or runtime errors.")

    finally:
        if path_added and abs_folder in sys.path:
            sys.path.remove(abs_folder)


def main() -> None:
    """Run main selection menu."""
    print("🌱 Welcome to Code Cultivation - Module 01 Helper! 🌱")
    print("This helper tests your Object-Oriented Garden exercises from the root folder.\n")
    print("Which exercise would you like to test?")
    print()
    print("0 - ft_garden_intro     (Ex0: Planting Your First Seed)")
    print("1 - ft_garden_data      (Ex1: Garden Data Organizer)")
    print("2 - ft_plant_growth     (Ex2: Plant Growth Simulator)")
    print("3 - ft_plant_factory    (Ex3: Plant Factory)")
    print("4 - ft_garden_security (Ex4: Garden Security System)")
    print("5 - ft_plant_types      (Ex5: Specialized Plant Types)")
    print("6 - ft_garden_analytics (Ex6: Garden Analytics)")
    print("a - Test all exercises")
    print()

    choice = input("Enter your choice: ").strip()

    if choice in EXERCISES:
        folder, file_name, title = EXERCISES[choice]
        test_ft_exercise(folder, file_name, title)
    elif choice == "a":
        for key in sorted(EXERCISES.keys()):
            folder, file_name, title = EXERCISES[key]
            test_ft_exercise(folder, file_name, title)
    else:
        print("❌ Invalid choice! Please enter 0, 1, 2, 3, 4, 5, 6, or a")


if __name__ == "__main__":
    main()
