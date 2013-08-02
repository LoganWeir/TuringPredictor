
# Usage: python scriptname inputfile outputfile
from sys import argv

script, infile, outfile = argv

text = open(infile)
product = open(outfile, 'a')

utterance = ""
 
for line in text:
  items = line.split()
  if len(items) == 5: 
    speaker = items[2] 
    if speaker == "b-wilcox-angela":
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
        utterance += "\n" + "program" + " |"
      elif this_addition == "BackSpace":
        utterance += " BackSpace " 
      # elif this_addition == "CR":
      #   utterance += "\n" + "program" + " |"
      else:
        utterance += this_addition
if utterance != "":
  product.write ("\n" + "program" + " |" + utterance)

product.close()

#2012 exclam = !
#2012 quoteright = '