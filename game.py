'''
DOCSTRINZG
Adventure Game
Author: Suryansha Basnet
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
'''


# Welcome message and introduction
print("Welcome to the Adventure Game!")  
print("Your journey begins here...")

# Ask for the player's name
player_name = input("what is your name,adventure?")

# Concatenate strings to create a personalized message
print("Welcome, " + player_name +"! Your journey begins now.")

# Use an f-string to display the same message in a more redable way
print(f"Welcome, {player_name}! Your journey begins now.")

#Describr the starting area
starting_area = """
You find yourself in a dark forest
The sound of rustling leaves fills the air
A faint path lies ahead, leading deeper into the
unknown...
"""
print(starting_area)

# Ask the player for their first decision
decision = input ("Do you wish to take a path (yes or no):")

print(decision)