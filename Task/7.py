# Task 4: The Airdrop Validator
# You are handling backend validation for an in-app purchase. 
# A user can get a premium bundle if they either have enough diamonds 
# OR they have an active special airdrop voucher.
# Given:
diamond_balance = 45
bundle_cost = 100
has_airdrop_voucher = True
account_banned = False
# Goal: Write a single boolean expression that evaluates to
# True if the user can get the item and is not banned.
# Assign it to a variable purchase_approved and print it.

purchase_approved = (diamond_balance >= bundle_cost or has_airdrop_voucher) and not account_banned
print(purchase_approved)