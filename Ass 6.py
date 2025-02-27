# Assignment 6 (21.02.25) min 50 LOC
# open topic code using any concept.

# Introduction
print("🔥 Welcome to the Kingdom of Eldoria! 🔥")
print("You are a brave warrior on a quest for treasure.")

# Variables
inventory = []  # List to store collected items
treasures = ("Golden Crown", "Magic Stone", "Ancient Sword")  # Tuple of treasures
attempts = 3  # Number of chances to escape danger

# Main Loop - Keeps the adventure going
while True:
    print("\nYou find yourself at a crossroads. What will you do?")
    print("1. Explore the Haunted Forest")
    print("2. Cross the Raging River")
    print("3. Enter the Abandoned Castle")
    print("4. Check Inventory")
    print("5. Quit the Adventure")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("\nYou step into the haunted forest. The trees whisper around you.")
        enemies = ["Shadow Beast", "Wicked Sorcerer", "Cursed Wolf"]
        enemy = enemies[len(inventory) % 3]  # Selects an enemy based on inventory size
        print(f"Suddenly, a {enemy} appears!")

        while attempts > 0:
            action = input("Do you (A) Fight or (B) Run? ").lower()
            if action == "a":
                print(f"You bravely battle the {enemy} and emerge victorious!")
                found_treasure = treasures[len(inventory) % 3]  # Selects a treasure based on inventory
                print(f"You found a {found_treasure}!")
                inventory.append(found_treasure)  # Add to inventory
                break
            elif action == "b":
                attempts -= 1
                print(f"You try to escape! Attempts left: {attempts}")
                if attempts == 0:
                    print("The enemy caught you! Game Over.")
                    break
            else:
                print("Invalid choice! Think fast!")

    elif choice == "2":
        print("\nYou stand before a raging river. The current is strong.")
        river_choices = ["Jump across the stones", "Build a raft", "Swim across"]

        for index in range(len(river_choices)):
            print(f"{index + 1}. {river_choices[index]}")

        river_choice = input("How do you cross? Choose (1/2/3): ")

        if river_choice == "1":
            print("You skillfully jump across the stones and make it safely.")
        elif river_choice == "2":
            print("You build a raft and paddle across successfully.")
            inventory.append("Wooden Shield")  # Adds an item for creative thinking
        elif river_choice == "3":
            print("The current is strong, but you manage to swim across.")
        else:
            print("Invalid choice! You slip and have to find another way.")

    elif choice == "3":
        print("\nYou enter the abandoned castle. Dust covers everything.")
        rooms = ["The Throne Room", "The Secret Dungeon", "The Treasury"]

        for room in rooms:
            print(f"- You enter {room}.")
            if room == "The Secret Dungeon":
                print("You find an enchanted key! It might unlock something.")
                inventory.append("Enchanted Key")
            elif room == "The Treasury":
                print("You discover a hidden chest filled with gold!")
                inventory.append("Bag of Gold")

        print("The castle creaks! You quickly leave before it collapses.")

    elif choice == "4":
        print("\nYour Inventory:")
        if inventory:
            for item in inventory:
                print(f"- {item}")
        else:
            print("Your inventory is empty!")

    elif choice == "5":
        print("You decide to end your journey. See you next time!")
        break  # Exit the loop

    else:
        print("Invalid choice! Try again.")
