# pet_game.py

from pet_logic import Dog, Cat, Hamster
import time

def choose_pet():
    print("Welcome to Virtual Pet Playground!")
    print("Choose your pet:")
    print("1. Dog")
    print("2. Cat")
    print("3. Hamster")

    while True:
        choice = input("Enter 1, 2, or 3: ")
        name = input("What will you name your pet? ")

        if choice == "1":
            print(f"\n🎉 You adopted a dog named {name}!")
            return Dog(name)
        elif choice == "2":
            print(f"\n🎉 You adopted a cat named {name}!")
            return Cat(name)
        elif choice == "3":
            print(f"\n🎉 You adopted a hamster named {name}!")
            return Hamster(name)
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

def game_loop(pet):
    while True:
        print(f"\nWhat would you like to do with {pet.name}?")
        print("1. Feed ")
        print("2. Play ")
        print("3. Wait ")
        print("4. Check Status ")
        print("5. Quit ")

        choice = input("Choose an option (1–5): ")

        if choice == "1":
            pet.feed()
            print(f"You fed {pet.name}!")
        elif choice == "2":
            pet.play()
            if hasattr(pet, "speak"):
                print(pet.speak())
        elif choice == "3":
            pet.tick()
            print("Time passes...")
        elif choice == "4":
            print(pet.get_status())
        elif choice == "5":
            print(f"Goodbye to {pet.name}! 👋")
            break
        else:
            print("Invalid choice.")

        time.sleep(1)

def main():
    pet = choose_pet()
    game_loop(pet)

if __name__ == "__main__":
    main()
