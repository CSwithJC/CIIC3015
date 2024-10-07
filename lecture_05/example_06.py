import timeit

# Create a tuple:
my_tuple = (1, 2, 3, "jean", "bienve")

# Access an element of the tuple:
print(my_tuple[4])

# Try to update a value of the tuple (This shouldn't work!):
# my_tuple[4] = "new string"

# Test how fast creating a tuple is compared to creating a list.
print(timeit.timeit('["test", "jean", "ok", "test", "jean", "ok"]', number=10000))
print(timeit.timeit('("test", "jean", "ok", "test", "jean", "ok")', number=10000))
