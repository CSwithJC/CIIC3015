# Open a file named philosophers.txt.
infile = open('philosophers.txt', 'r')

# Read three lines from the file.
line1 = infile.readline()
line2 = infile.readline()
line3 = infile.readline()

# Strip the \n from each string.
line1 = line1.rstrip('\n')
line2 = line2.rstrip('\n')
line3 = line3.rstrip('\n')

# Close the file.
infile.close()

# Print the data that was read into memory.
print(line1)
print(line2)
print(line3)