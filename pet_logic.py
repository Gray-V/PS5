# This file defines the logic for a virtual pet game.
# We will create a base class for all pets 
# and then define specific pet types (Dog, Cat, Hamster) that inherit from the base class.
# We use super() to share behavior from the base pet class.

import random

# STEP 1: Define the base class that all pets inherit from
class BasePet:
    def __init__(self, name, species):
        # HINT: Use the self keyword to define instance variables
        # TODO: Each pet has a name and species (like "dog" or "cat")
        # Use the constructor to init these properties
        self.name = name
        self.species = species

        # TODO: All pets start with default hunger and happiness values of 5
        # Initialize hunger and happiness as instance variables
        # The default to add or subtract hunger and happiness is 2
        
        self.hunger = 5        # 0 = full, 10 = starving
        self.happiness = 5     # 0 = sad, 10 = happy

    def feed(self):
        # TODO: 
        # Feeding fills hunger
        # Make sure hunger doesn't go over 10 or below 0
        self.hunger = max(0, self.hunger - 2)

    def play(self):
        # Playing increases happiness
        # Make sure hunger doesn't go over 10 or below 0
        self.happiness = min(10, self.happiness + 2)


# Do not change this method
    def tick(self):
        # Simulates time passing
        self.hunger = min(10, self.hunger + 1)
        self.happiness = max(0, self.happiness - 1)
# Continue below this line

    def get_status(self):
        return f"{self.name} the {self.species} — Hunger: {self.hunger}, Happiness: {self.happiness}"


# 🐶 STEP 2: Dog inherits from BasePet
class Dog(BasePet):
    def __init__(self, name):
        # ✅ Use super() to call BasePet’s constructor
        super().__init__(name, "dog")

    def play(self):
        # 🐾 Dogs love to play and get extra happy!
        self.happiness = min(10, self.happiness + 3)

    def speak(self):
        return f"{self.name} says: Woof!"


# 🐱 STEP 3: Cat inherits from BasePet
class Cat(BasePet):
    def __init__(self, name):
        # ✅ Call BasePet’s constructor using super()
        super().__init__(name, "cat")

    def play(self):
        # 🐾 Cats are picky — sometimes they don't enjoy play
        if random.random() > 0.5:
            self.happiness = min(10, self.happiness + 2)
        else:
            self.happiness -= 1
            print(f"{self.name} ignored you. Typical cat.")

    def speak(self):
        return f"{self.name} says: Meow."


# 🐹 STEP 4: Hamster inherits from BasePet
class Hamster(BasePet):
    def __init__(self, name):
        super().__init__(name, "hamster")

    def play(self):
        # 🐾 Hamsters roll around in their ball and get happy!
        self.happiness = min(10, self.happiness + 1)
        self.hunger += 1  # they get hungry from running

    def speak(self):
        return f"{self.name} squeaks excitedly!"
