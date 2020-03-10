"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
file = open("foo.txt", "r")
print(file.read())

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
# opens file
f = open("bar.txt", "w")
# this adds lines
f.write('''My precious. 
Oh my PRECIOUS... 
No's yous can'ts haves it!!MINE!!''')
f.close
# checks for lines
f = open("bar.txt", "r")
print(f.read())

# import os

# def read_file(file):
#     try:
#         filee = os.path.dirname(__file__)

#         txt = open(f"{filee}/{file}", "r")
#         read_text = txt.read()
#         txt.close()
#         return read_text
#     except FileExistsError:
#         print(f"{FileNotFoundError}")
# print(read_file("foo.txt"))

# fp = open("bar.txt", "w")

# fp.write("""My precious.
# Oh my PRECIOUS...
# No's yous can'ts haves it!!MINE!!""")

# # Close the file
# fp.close()
