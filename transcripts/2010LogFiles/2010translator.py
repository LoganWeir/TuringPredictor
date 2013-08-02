
# Usage: python scriptname inputfile outputfile author position
from sys import argv
import csv

script, infile, outfile, author, position = argv

text = open(infile)
product = open(outfile, 'a')

# comment out if OP OP OP OP, OPA VOPAL STYLE
writer = csv.writer(product)

utterance = ""

for line in text:
  items = line.split()
  if len(items) == 5: 
    speaker = " ".join(items[2:4]) 
    if speaker == "%s" % position:
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
        utterance += " "
      elif this_addition == "BackSpace":
        utterance += " BackSpace " 
      elif this_addition == "CR":
        writer.writerow ([author , utterance])
        utterance = ""
      #HEEEEEEEEEEEEEY SEXY LAAAADYYYY
      # elif this_addition == "CR":
      #   utterance += "\n" + author + " |"   
      else:
        utterance += this_addition
if utterance != "":
  writer.writerow ([author , utterance])

#OPA VOPAL STYLE:
# if utterance != "":
#   product.write ("\n" + author + " |" + utterance)

product.close()

