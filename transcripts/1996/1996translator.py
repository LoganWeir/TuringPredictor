
# Usage: python scriptname inputfile outputfile author position
from sys import argv
import csv

script, infile, outfile, author = argv

text = open(infile)
product = open(outfile, 'a')

# comment out if OP OP OP OP, OPA VOPAL STYLE
writer = csv.writer(product)

utterance = ""
start = "<start> "

for line in text:
	if line[0:3] == "CON":
		utterance = line[17:]
		writer.writerow ([author, start+utterance])

product.close()
