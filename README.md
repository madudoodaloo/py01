Building on your Python fundamentals from the first activity, you’ll now tackle more
complex programming challenges by creating a comprehensive garden data management
system. This project introduces advanced concepts that make Python a powerful tool for
modeling real-world systems.
You’ll work on:
• Understanding how Python programs are structured and executed
• Organizing data using an object-oriented approach
• Creating reusable code components
• Building systems that can adapt and extend
• Protecting data integrity in collaborative environments
• Designing scalable software architectures
Each exercise builds on the previous ones, creating a complete digital garden ecosystem
by the end.

IMPORTANT: This module starts with basic Python program structure,
then progresses to Object-Oriented Programming. Each exercise should
contain the requested definitions and any required code. You may
include simple test code at the bottom of each file using if __name__
== "__main__": blocks for your own testing.



okay let's go back to py01 ex5, do the usual presentation:
subject analysis and oop terminology and key concepts expected to know on this exercise, and then the resolution and guidelines for further investigation to understand proper python programming practices


• python programs starting point: if __name__ == "__main__" blocks - why is this line important? understand how programs start and execute
• shebang line and directly executable scripts
• classes, attributtes, instancing a class and settign specific values to the attributes, methods of a class
• instantiate and initializing a class, construction
• secure system that protects and encapsulates sensitive data: getters and setters; use encapsulation to prevent your class attributes from being used directly with the protected convention (not the mangling)
• inheritance from a parent category, calling parent methods through super, our method override can re-use the already existing code in the parent, code reusability
• complex data relationships, nested components and inheritance chains
• static methods, class methods, internal systems implemented as nested classes, decorator syntax

• Programming Concept Mastery:
• Can the learner explain how Python programs are structured?
• Do they understand the difference between classes and objects?
• Do they understand when and why to use inheritance?
• Can they explain encapsulation benefits?
• Do they understand method types (instance, class, static)?
• Class definition with proper syntax
• Object instantiation (creating instances)
• Ask the learner to explain what methods are and why they used them
• Method definition within classes
• Method calls on object instances
• State changes through method execution
• Simulation logic using methods
• __init__ method definition and usage
• Parameter passing during object creation
• Verify the program uses __init__ method for object initialization
• Ask the learner to explain what __init__ does and why it's needed
• Base class (Plant) with common features
• Derived classes (Flower, Tree, Vegetable) with specialized features
• super() calls to parent class methods
• Method overriding for specialized behavior
• Verify distinction between member and non-member functions
• Nested classes (class within a class)
• Inheritance chains (A -> B -> C)
• Class methods (using classmethod()) vs instance methods
• Static methods (using staticmethod()) vs regular functions
• Non-member functions (outside any class)
• Class methods can create instances without decorators
• Static methods work without instance using traditional syntax
• Non-member functions operate on class instances

Advanced concepts discussion:
• Ask about when to use each type of method
• Discuss the benefits of nested classes
• Explain the inheritance chain design choices
