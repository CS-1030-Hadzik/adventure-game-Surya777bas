'''
DOCSTRING
Adventure Game
Author: Suryansha Basnet
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
'''

import random

# Player class to manage health and inventory
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100  # Starting health
        self.inventory = []  # Inventory to store items

# Function to check if the player has lost (health <= 0)
def check_lose(player):
    if player.health <= 0:
        print(f"\nOh no, {player.name}! Your health reached 0. Game over. ")
        exit()

# Function to decrease health if the player stays still
def stay_still(player):
    print("You stay still, listening to the forest...")
    player.health -= 10  # Decrease health
    print("You lost 10 health from boredom.")
    check_lose(player)  # Check if health is 0 or below

# Function to explore the dark woods
def explore_dark_woods(player):
    print(f"{player.name}, you step into the dark woods.")
    print("The trees whisper as you walk deeper.")
    # Random event: find an item or lose health
    if random.choice([True, False]):  # 50% chance to find an item
        item = "map"
        if item not in player.inventory:
            player.inventory.append(item)
            print(f"You found a {item}! It will help you navigate the forest.")
        else:
            print("You already have a map.")
    else:
        stay_still(player)  # Decrease health if nothing happens

# Function to explore the mountain pass
def explore_mountain_pass(player):
    print(f"{player.name}, you make your way towards the mountain pass.")
    print("The cold wind brushes against your face.")
    # Random event: find an item or lose health
    if random.choice([True, False]):  # 50% chance to find an item
        item = "lantern"
        if item not in player.inventory:
            player.inventory.append(item)
            print(f"You found a {item}! It will light your way in dark areas.")
        else:
            print("You already have a lantern.")
    else:
        stay_still(player)  # Decrease health if nothing happens

# Function to heal the player
def use_heal_item(player):
    if "healing potion" in player.inventory:
        player.health += 20
        player.inventory.remove("healing potion")
        print("You used a healing potion and restored 20 health.")
    else:
        print("You don't have a healing potion in your inventory.")

# Main Game Loop
def main():
    print("Welcome to the Adventure Game!")
    player_name = input("What is your name, adventurer? ")
    player = Player(player_name)

    print(f"Welcome, {player.name}! Your journey begins now.")
    starting_area = """
    You find yourself in a dark forest.
    The sound of rustling leaves fills the air.
    A faint path lies ahead, leading deeper into the unknown...
    """
    print(starting_area)

    while True:
        print(f"\nHealth: {player.health}")  # Display current health
        print(f"Inventory: {player.inventory}")
        print("\nYou see two paths ahead:")
        print("\t1. Take the left path into the dark woods.")
        print("\t2. Take the right path towards the mountain pass.")
        print("\t3. Stay where you are.")
        print("\t4. Use a healing potion (if you have one).")

        decision = input("What will you do? (1, 2, 3, 4): ").strip()

        if decision == "1":
            explore_dark_woods(player)  # Go to the dark woods
        elif decision == "2":
            explore_mountain_pass(player)  # Go to the mountain pass
        elif decision == "3":
            stay_still(player)  # Stay still and lose health
        elif decision == "4":
            use_heal_item(player)  # Use healing item
        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")

        # Ask if the player wants to continue exploring
        play_again = input("Do you want to continue exploring? (yes or no): ").lower()
        if play_again != "yes":
            print(f"Thanks for playing, {player.name}! See you next time.")
            break  # Exit the loop and end the game

if __name__ == "__main__":
    main()