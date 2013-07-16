# Usage: python scriptname outputfilename

#text, human or program or judge(relevant?)

import csv
import sys

infile = open(sys.argv[1], 'r')
##outfile = open(sys.argv[2], 'w')

line = infile.readline()

letter_data = {}

while (line  != ""): 
	if (line.strip() == ""):
		infile.readline()
		continue

	letter = line.split()[-1]

for letter in letter_data.items():
	letter = letter.replace("space", " ")
	words = "".join(letter)
#line = infile.readline()


print words


##writer = csv.writer(outfile)