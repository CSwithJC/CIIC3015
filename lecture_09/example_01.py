# Open a file named philosophers.txt.
outfile = open('philosophers.txt', 'w')

# Write the names of three philosphers
# to the file.
outfile.write('John Locke\n')
outfile.write('David Hume\n')
outfile.write('Edmund Burke\n')

# Close the file.
outfile.close()