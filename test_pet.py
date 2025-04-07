import pytest
from pet_logic import BasePet, Dog, Cat, Hamster

# Test the BasePet constructor
def test_constructor():
    pet = BasePet("Buddy", "lizard")
    assert pet.name == "Buddy"
    assert pet.species == "lizard"
    assert pet.hunger == 5
    assert pet.happiness == 5

# Test the feed() method on BasePet
def test_feed():
    pet = BasePet("Buddy", "lizard")
    pet.hunger = 6
    pet.feed()
    assert pet.hunger == 4
    pet.feed()
    assert pet.hunger == 2
    pet.feed()
    assert pet.hunger == 0
    pet.feed()  # Should not go below 0
    assert pet.hunger == 0

# Test the play() method on BasePet
def test_play():
    pet = BasePet("Buddy", "lizard")
    pet.happiness = 8
    pet.play()
    assert pet.happiness == 10
    pet.play()  # Should not go above 10
    assert pet.happiness == 10

# Test Dog's play() method
def test_dog_play():
    dog = Dog("Rex")
    dog.happiness = 5
    dog.play()
    assert dog.happiness == 8
    dog.play()
    assert dog.happiness == 10

# Test Dog's speak() method
def test_dog_speak():
    dog = Dog("Rex")
    assert dog.speak() == "Rex says: Woof!"

# Test Cat's play() with monkeypatch to force outcome
def test_cat_play_happy(monkeypatch):
    cat = Cat("Whiskers")
    cat.happiness = 5
    monkeypatch.setattr("random.random", lambda: 1.0)
    cat.play()
    assert cat.happiness == 7

def test_cat_play_ignore(monkeypatch):
    cat = Cat("Whiskers")
    cat.happiness = 5
    monkeypatch.setattr("random.random", lambda: 0.0)
    cat.play()
    assert cat.happiness == 4

# Test Cat's speak() method
def test_cat_speak():
    cat = Cat("Whiskers")
    assert cat.speak() == "Whiskers says: Meow."

# Test Hamster's play() method
def test_hamster_play():
    hamster = Hamster("Nibbles")
    hamster.hunger = 3
    hamster.happiness = 4
    hamster.play()
    assert hamster.hunger == 4
    assert hamster.happiness == 6

# Test Hamster's speak() method
def test_hamster_speak():
    hamster = Hamster("Nibbles")
    assert hamster.speak() == "Nibbles says: Squeak!"
