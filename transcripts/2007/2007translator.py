
# Usage: python scriptname inputfile outputfile author position
from sys import argv
import csv

script, infile, outfile, author, position = argv

text = open(infile)
product = open(outfile, 'a')

# comment out if OP OP OP OP, OPA VOPAL STYLE
writer = csv.writer(product)

utterance = ""
start = "<start> "
end = " <end>"

for line in text:
  items = line.split()
  if len(items) == 6: 
    speaker = " ".join(items[3:5]) 
    if speaker == "%s" % position:
      this_addition = items[5]
      if this_addition == "space":
        utterance += " "
      elif this_addition == "BackSpace":
        utterance = utterance[:-1]
      elif this_addition == "CR":
        length = len(utterance.split())
        writer.writerow ([author , start+utterance+end , length])
        utterance = ""
      #HEEEEEEEEEEEEEY SEXY LAAAADYYYY
      # elif this_addition == "CR":
      #   utterance += "\n" + author + " |"   
      else:
        utterance += this_addition
if utterance != "":
  length = len(utterance.split())
  writer.writerow ([author , start+utterance+end, length])

#OPA VOPAL STYLE:
# if utterance != "":
#   product.write ("\n" + author + " |" + utterance)

product.close()

