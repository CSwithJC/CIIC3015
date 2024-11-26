filename = input('Enter a filename: ')
try:
 # Open the file.
 infile = open(filename, 'r')
 # Read the file's contents.
 contents = infile.read()
 # Display the file's contents.
 print(contents)
 # Close the file.
 infile.close()
except IOError:
 print('An error occurred trying to read')
 print('the file', filename)