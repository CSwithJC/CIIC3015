# Create a dictionary with prices.
prices = {'burrito': 10.00, 'hamburger': 10.00}

# Add some items alongside their prices.
prices['water'] = 1.00
prices['soda'] = 2.00

print("Prices dictionary after adding more items:")
print(prices)

# We are out of stock of hamburgers! Remove them from our prices.
prices.pop('hamburger')
print(prices)

# Inflation is bad! Let's update the prices our burritos.
prices['burrito'] = 12.00
print(prices)

# Access the price of an item:
water_price = prices['water']
print(f'The price of a bottle of water is: {water_price}')