# Task 3: The Inventory Sorter
# You are writing a backend script for a game where items stack in sets of 64.
# Given:

# Python
total_iron_mined = 412
stack_limit = 64
# Goal: Calculate how many full stacks the player has, and
# how many loose iron ingots are left over in the current slot.
# Print: "Inventory: [X] full stacks, [Y] loose items".

FullStack = total_iron_mined // stack_limit
loose = total_iron_mined % stack_limit
print(f"Inventory: {FullStack} full stacks, {loose} loose items")