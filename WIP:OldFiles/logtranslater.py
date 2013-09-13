
# Usage: python scriptname inputfile outputfile
from sys import argv
import csv
import numpy as np

script, infile, outfile = argv

text = open(infile)
product = open(outfile, 'w')

product.truncate()

speaker = ""
utterance = ""
 
for line in text:
  items = line.split()
  if len(items) == 5:
    this_speaker = " ".join(items[2:4])
    if this_speaker != speaker:
      if utterance != "":
        product.write ("\n" + speaker + ": " + utterance)
      speaker = this_speaker
      utterance = ""
    this_addition = items[4]
    if this_addition == "space":
      utterance += " "
    elif this_addition == "question":
      utterance += "?"
    elif this_addition == "comma":
      utterance += ","
    elif this_addition == "period":
      utterance += "."
    elif this_addition == "Return":
      utterance += ""
    elif this_addition == "BackSpace":
      utterance = utterance[:-1]
    else:
      utterance += this_addition
if utterance != "":
  product.write ("\n" + speaker + ": " + utterance)

#outfile = open(sys.argv[2], 'w')

#writer = csv.writer(outfile)

#for line in transcript:
	#writer.writerow(line)

#outfile.close()
