# The Ride Fare Estimator
# You are building the pricing module for a ride-hailing app operating out of Maninagar.
# Given:

# Python
base_fare = 45.0
per_km_rate = 14.5
distance_km = 8.2
surge_multiplier = 1.2
# Goal: Calculate the total fare (base fare + distance cost, all multiplied by the surge).
# Print the result formatted to 2 decimal places using an f-string: "Total Fare: ₹[amount]".

distanceCost = per_km_rate * distance_km
subtotal = distanceCost + base_fare
total = subtotal * surge_multiplier

# total = ((per_km_rate * distance_km) + base_fare) // surge_multiplier
print(f"Total Fare: ₹{total:.2f}")