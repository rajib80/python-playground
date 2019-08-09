# Open the file mbox-short.txt and read it line by line.
# When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split()
# and print out the second word in the line
# (i.e. the entire address of the person who sent the message).
# Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.
# You can download the sample data at
# http://www.py4e.com/code3/mbox-short.txt

file_handle = open("mbox-short.txt")

line_count = 0

for line in file_handle:
    if not line.startswith("From:") and line.startswith("From"):
        words = line.split()
        print(words[1])
        line_count += 1

print(f"There were {line_count} lines in the file with From as the first word")
