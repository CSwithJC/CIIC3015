prices = {'burrito': 10.0, 'hamburger': 10.0, 'water': 1.0, 'soda': 2.0}

# Iterate through all keys:
print('Iterate through all keys!')
for key in prices:
    print(key)

# Iterate through all values:
print('\nIterate through all values!')
for value in prices.values():
    print(value)

# Iterate through both keys and values (at once):
print('\nIterate through all values!')
for key, value in prices.items():
    print(f'The current key is: {key} and it\'s value is: {value}')

# Increase the price of all food based on an inflation rate!
inflation_rate = 0.06  # Prices increased year-over-year by 6%
print('\nIncrease the price of all items based on an inflation rate.')
for key in prices:
    prices[key] = prices[key] + (prices[key]*inflation_rate)
    print(f'The new price for {key} is: {prices[key]}')

# Count the letters in a string.
print('\nCount the number of letters in a string.')
sentence = 'Hello how are you today'
letter_count = {}
for letter in sentence:
 if letter in letter_count:
   letter_count[letter] = letter_count[letter] + 1
 else:
   letter_count[letter] = 1
print(letter_count)

