**CMSI 1010** Computer Programming & Laboratory, Spring 2025

# Problem Set 5

**Due 11:59pm PT 4/09**

---

## Programming

1. **Shape Spawner** – `shape_spawner.py`

   As you explore Python classes and object-oriented programming, it’s time to level up with Pygame! In this assignment, you’ll build a simple visual application using Pygame where clicking buttons spawns different shapes that behave based on parameters passed to a single class.

   You’ll create a flexible `GameObject` class and instantiate different shapes by modifying constructor arguments like shape type, color, speed, and more.

---

### Requirements

1. **Create a `GameObject` class**  
   This class will represent all the spawned objects (e.g., circles and squares) and should support different behaviors based on parameters like shape, speed, and color.

   Your class must include:

   ```python
   def __init__(self, x, y, shape, size, color, speed):  # Initialize object attributes
       ...

   def move(self):  # Update position based on speed
       ...

   def draw(self, screen):  # Draw the shape on screen
       ...
   ```

2. **Create a Pygame interface**  
   - The screen should display at least two clickable buttons (e.g., "Spawn Red Circle", "Spawn Blue Square").
   - Clicking a button should create and spawn a new `GameObject` with unique parameters.
   - Objects should immediately begin moving based on their `speed` parameter.

3. **Visual behavior and interactivity**  
   - Spawned shapes should continue moving independently.  
   - Each instance should behave based on how it was initialized (e.g., different speeds, sizes, shapes).

4. **Minimum feature set**  
   - At least two buttons for spawning different object types  
   - At least one movement or behavior difference between object types


---

### Unit Testing

There is no formal test script for this assignment, but your code should:

- Run without errors  
- Clearly display shapes that behave differently  
- Demonstrate your understanding of parameterized class behavior

---


---

## Points breakdown

| Category                     | Points                        |
|-----------------------------|-------------------------------|
| GameObject class            | 25                            |
| Object spawning and behavior| 25                            |
| Button interface            | 20                            |
| Distinct object behaviors   | 20                            |
| **Total**                   | **100**                       |
