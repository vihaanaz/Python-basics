import sys
import getopt
import argparse

# --------------------
# File Reading: Full content
f = open("demofile.txt", "r")
print(f.read())
f.close()

# --------------------
# File Reading: First 5 characters
f = open("demofile.txt", "r")
print(f.read(5))
f.close()

# --------------------
# File Reading: Line by line
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())
f.close()

# --------------------
# File Reading: Loop through lines
f = open("demofile.txt", "r")
for x in f:
    print(x.strip())  # strip() removes extra newlines
f.close()

# --------------------
# File Writing: Append to file
f = open("demofile2.txt", "a")
f.write("Now the file has more content!\n")
f.close()

# --------------------
# File Reading: Read the new content
f = open("demofile2.txt", "r")
print(f.read())
f.close()

# --------------------
# File pointer position
f = open("demofile.txt", "r")
print(f.read())
print("Pointer position:", f.tell())
f.close()

# --------------------
# File Reading: Read specific parts
f = open("demofile.txt", "r")
print(f.read(5))    # Read first 5 chars
print(f.read(10))   # Then next 10 chars
print("Pointer position:", f.tell())
f.close()

# --------------------
# Command-line Arguments
n = len(sys.argv)
print("Total arguments passed:", n)
print("Name of Python script:", sys.argv[0])

print("Arguments passed:", end=" ")
for i in range(1, n):
    print(sys.argv[i], end=" ")

Sum = 0
for i in range(1, n):
    Sum += int(sys.argv[i])
print("\nResult:", Sum)

# --------------------
# Option Parsing with getopt
argument = sys.argv[1:]
options = "hmo"
long_options = ["help", "move", "open"]

try:
    arguments, values = getopt.getopt(argument, options, long_options)

    for currentArgument, currentValue in arguments:
        if currentArgument in ("-h", "--help"):
            print("Help argument")
        elif currentArgument in ("-m", "--move"):
            print("Move argument")
        elif currentArgument in ("-o", "--open"):
            print("Open argument")
        else:
            print("Unknown option:", currentArgument)

except getopt.GetoptError as err:
    print("Error:", str(err))

    msg = "Adding description"
    parser = argparse.ArgumentParser(description=msg)
    parser.parse_args()