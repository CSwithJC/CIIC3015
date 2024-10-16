# Create an empty set of countries.
countries = set()

# Add a few countries (and add them multiple times)
countries.add('Argentina')
countries.add('Argentina')
countries.add('Brazil')
countries.add('Brazil')
countries.add('Brazil')
countries.add('Canada')
countries.add('Canada')
countries.add('Canada')
countries.add('Canada')
countries.add('England')
countries.add('England')
countries.add('England')
countries.add('Puerto Rico')
countries.add('Puerto Rico')
countries.add('Puerto Rico')
countries.add('Puerto Rico')
countries.add('Puerto Rico')
print(countries)

# Iterate the countries (notice the order of them)
print('\nIterate through the countries (and notice their order!)')
for country in countries:
    print(country)

# Remove a country.
print('\nRemove a specific country (England)')
countries.remove('England')
print(countries)

# Remove a random country.
print('\nRemove a random country.')
removed_country = countries.pop()
print(f'Just removed {removed_country} and the remaining countries are {countries}')
