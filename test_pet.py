# test_pet_logic.py

import pytest
from pet_logic import Dog, Cat, Hamster, BasePet

def test_dog_inherits_basepet():
    d = Dog("Rex")
    assert isinstance(d, BasePet)
    assert d.species == "dog"
    assert d.name == "Rex"

def test_dog_play_increases_happiness():
    d = Dog("Rex")
    old_happiness = d.happiness
    d.play()
    assert d.happiness == min(10, old_happiness + 3)

def test_cat_play_random():
    c = Cat("Luna")
    # Run multiple times to catch both branches of randomness
    happy_results = set()
    for _ in range(10):
        c.happiness = 5
        c.play()
        happy_results.add(c.happiness)
    assert 4 in happy_results or 7 in happy_results

def test_hamster_play_behavior():
    h = Hamster("Nibbles")
    old_happiness = h.happiness
    old_hunger = h.hunger
    h.play()
    assert h.happiness == min(10, old_happiness + 1)
    assert h.hunger == old_hunger + 1

def test_tick_and_feed():
    p = Dog("Shadow")
    p.hunger = 5
    p.happiness = 5
    p.tick()
    assert p.hunger == 6
    assert p.happiness == 4
    p.feed()
    assert p.hunger == 4
