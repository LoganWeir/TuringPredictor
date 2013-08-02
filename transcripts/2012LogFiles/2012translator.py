
# Usage: python scriptname inputfile outputfile author position
from sys import argv
import csv

script, infile, outfile, author, position = argv

text = open(infile)
product = open(outfile, 'a')

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
      elif this_addition == "quoteright":
        utterance += "'"
      elif this_addition == "quotedbl":
        utterance += "\""  
      elif this_addition == "exclam":
        utterance += "!"
      elif this_addition == "parenleft":
        utterance += "("
      elif this_addition == "parenright":
        utterance += ")"
      elif this_addition == "BackSpace":
        utterance += " BackSpace "
      elif this_addition == "backslash":
        utterance += "\\"
      elif this_addition == "minus":
        utterance += "-" 
      elif this_addition == "Return":
        writer.writerow ([author , utterance])
        utterance = ""
      # elif this_addition == "Return":
      #   utterance += "\n" + author + " |"   
      else:
        utterance += this_addition
if utterance != "":
  writer.writerow ([author , utterance])

# if utterance != "":
#   product.write ("\n" + author + "," + utterance)

product.close()

#2012 exclam = !
#2012 quoteright = '
#backslash?

#sys argv for program position?