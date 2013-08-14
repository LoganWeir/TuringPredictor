
# Usage: python scriptname inputfile outputfile author position
from sys import argv
import csv

script, infile, outfile, author = argv

text = open(infile)
product = open(outfile, 'a')

writer = csv.writer(product)

utterance = ""
start = "<start> "
end = " <end>"

for line in text:
	line = line.strip()
	if line[0:3] == "PRO":
		utterance = line[17:]
		length = len(utterance.split())
		writer.writerow ([author , start+utterance+end , length])

# for line in text:
# 	line = line.strip()
# 	if line[0:3] == "PRO":
# 		utterance = line[17:]
# 		writer.writerow ([author, start + utterance])

product.close()
