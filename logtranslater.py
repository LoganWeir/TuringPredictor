# Usage: python scriptname outputfilename

#text, human or program or judge(relevant?)

import csv
import sys

infile = open(sys.argv[1], 'r')
##outfile = open(sys.argv[2], 'w')

letter_data = {}

line =infile.readline()

with infile:
	letter = line.split()[-1] 

#for line in infile


#line = infile.readline()



#while (line  != ""): 
#	if (line.strip() == ""):
#		infile.readline()
#		continue

#	letter = line.split()[-1]

for letter in letter_data.items():
	letter = letter.replace("space", " ")
	
words = "".join(letter)

#line = infile.readline()


print words


##writer = csv.writer(outfile)