# IPO Allotment Logic
# You are writing a script for a brokerage platform to calculate how many shares a user can bid for.
# Given:
account_balance = 125000
lot_size = 65
price_per_share = 225
# Goal: Calculate the cost of one full lot.
# Then, using floor division and modulo, calculate exactly how many full lots the user can afford,
# and how much cash will be left in their account.
# Print both numbers.
account_balance = 125000
lot_size = 65
price_per_share = 225

# Cost of one lot
oneFullLot = lot_size * price_per_share
print("Lot Price:", oneFullLot)

# Full lots user can buy
userAfford = account_balance // oneFullLot
print("User Afford Lots:", userAfford)

# Remaining money
left = account_balance % oneFullLot
print("Amount Left:", left)