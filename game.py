'''
DOCSTRING
Adventure Game
Author: Suryansha Basnet
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
'''

# Player class to manage health and inventory
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100  # Starting health
        self.inventory = []

# Function to check if the player has lost (health <= 0)
def check_lose(player):
    if player.health <= 0:
        print(f"\n💀 Oh no, {player.name}! Your health reached 0. Game over. 💀")
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
    stay_still(player)  # For demonstration, let's say staying still in the woods decreases health

# Function to explore the mountain pass
def explore_mountain_pass(player):
    print(f"{player.name}, you make your way towards the mountain pass.")
    print("The cold wind brushes against your face.")
    stay_still(player)  # For demonstration, staying still in the mountain pass decreases health

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

        decision = input("What will you do? (1, 2, 3): ").strip()

        if decision == "1":
            explore_dark_woods(player)  # Go to the dark woods and potentially lose health
        elif decision == "2":
            explore_mountain_pass(player)  # Go to the mountain pass and potentially lose health
        elif decision == "3":
            stay_still(player)  # Stay still and lose health from boredom
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

        # Ask if the player wants to continue exploring
        play_again = input("Do you want to continue exploring? (yes or no): ").lower()
        if play_again != "yes":
            print(f"Thanks for playing, {player.name}! See you next time.")
            break  # Exit the loop and end the game

if __name__ == "__main__":
    main()
