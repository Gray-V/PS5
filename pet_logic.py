# This file defines the logic for a virtual pet game.
# We will create a base class for all pets 
# and then define specific pet types (Dog, Cat, Hamster) that inherit from the base class.
# We use super() to share behavior from the base pet class.

# Each test is worth 6 points! Do not forget to run the tests!

import random

# STEP 1: Define the base class that all pets inherit from
class BasePet:
    def __init__(self, name, species):
        # HINT: Use the self keyword to define instance variables
        # Each pet has a name and species (like "dog" or "cat")
        # TODO: Use the constructor to init these two properties
   

        # All pets start with default hunger and happiness values of 5
        # TODO: Initialize hunger and happiness as instance variables
        # The default to add or subtract hunger and happiness is 2
        pass

    def feed(self):
        # TODO: 
        # Feeding makes hunger two less
        # Make sure hunger doesn't go over 10 or below 0
        pass

    def play(self):
        # TODO: 
        # Playing increases happiness by 2
        # Make sure hunger doesn't go over 10 or below 0
        pass


# Do not change this method
    def tick(self):
        # Simulates time passing
        self.hunger = min(10, self.hunger + 1)
        self.happiness = max(0, self.happiness - 1)

    def get_status(self):
        # Print the pet's status
        return f"{self.name} the {self.species} — Hunger: {self.hunger}, Happiness: {self.happiness}"
# Continue below this line


# STEP 2: Dog inherits from BasePet
class Dog(BasePet):
    def __init__(self, name):
        # Use super() to call BasePet’s constructor
        # Done for you this time! Make sure to use it below!
        super().__init__(name, "dog")

    def play(self):
        # Dogs love to play and get extra happy!
        # TODO: Increase happiness by 3
        # Make sure happiness doesn't go over 10
        pass

    def speak(self):
        # Dogs bark when they are happy
        # TODO: Return a string that says "name says: Woof!"
        # Make sure the name is the pet's name
        return None


# STEP 3: Cat inherits from BasePet
class Cat(BasePet):
    def __init__(self, name):
        # TODO:
        # Call BasePet’s constructor using super()
        pass

    def play(self):
        # Cats are picky — sometimes they don't enjoy play
        # TODO: Use random.random() to decide if the cat plays
        # If the cat plays, increase happiness by 2
        # If the cat ignores you, decrease happiness by 1
        # Make sure happiness doesn't go over 10 or below 0
        pass

    def speak(self):
        # TODO: 
        # Cats meow when they speak
        # Return a string that says "name says: Meow."
        # Make sure the name is the pet's name
        return None


# STEP 4: Hamster inherits from BasePet
class Hamster(BasePet):
    def __init__(self, name):
        # TODO:
        # Call BasePet’s constructor using super()
        pass

    def play(self):
        # Hamsters roll around in their ball and get happy!
        # This is a fun activity for them but makes them hungry.
        # TODO: Increase happiness by 2 and increase hunger by 1
        # Make sure hunger doesn't go over 10
        # Make sure happiness doesn't go over 10
        pass

    def speak(self):
        # TODO:
        # Hamsters squeak when they speak
        # Return a string that says "name says: Squeak!"
        # Make sure the name is the pet's name
        return None
