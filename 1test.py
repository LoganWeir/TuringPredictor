
# Usage: python scriptname inputfile outputfile

import numpy as np
import pandas as pd
import csv
from sys import argv
import pickle

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import cross_val_score

script, infile, outfile = argv
#outfile

data = pd.read_csv("%s" % infile)

vectorizer = CountVectorizer(ngram_range=(1,2), token_pattern=r'\b\w+\b')

# strip_accents='unicode', 
#token_pattern=u'(?u)\b\w\w+\b'

speaker = data['speaker']

speaker = [1 if x == 'human' else 0 for x in speaker]

# speaker = np.array(speaker)

utterance = data['utterance']

train = vectorizer.fit_transform(utterance)

train = train.toarray()

length = data['length']

final = train.append(length)

model = LogisticRegression(class_weight={1:0.3475, 0:0.6525})
#With tokencombinedtext: class_weight={1:0.405, 0:0.595}

classifier = model.fit(final, speaker)

# userinput = raw_input("How are you doing today? ")

# userinput = "<start> " + userinput

# userinput = userinput.toarray()

# userinput2 = raw_input("What do you think of the Turing Test? ")

# userinput2 = "<start> " + userinput2

# userinput = np.array(userinput, userinput2, dtype=str)

# vectorizer1 = CountVectorizer(strip_accents='unicode', ngram_range=(1,2))

# train1 = vectorizer.transform([userinput])

# close = classifier.predict_proba(train1.toarray())

# print close[:,1:]

# humanity = close[:,1:]

# print "You are %r percent human" % (humanity)

print (cross_val_score(model, train.toarray(), speaker, cv = 5).mean())

# p = pickle.dump(classifier, open("save.p", "wb"))

pickle.dump(classifier, open("save.p","wb"))

pickle.dump(vectorizer, open("save2.p","wb"))

coefs = sorted(zip(classifier.coef_.T , vectorizer.get_feature_names()), reverse=True)

outfile = open(outfile, 'w')

writer = csv.writer(outfile)

for coef, name in coefs:
	writer.writerow([name, coef])

# coef1 = np.array(coef1)

# coef = np.reshape(coef1, (9858,1))

# tokens = vectorizer.get_feature_names()

# tokens = np.reshape(tokens, (9858,1))

# coefwords1 = np.hstack((tokens , coef))

# headers = np.array(['tokens','coef'])

# coefwords = np.vstack((headers, coefwords1))

# outfile = open(outfile, 'w')

# writer = csv.writer(outfile)


# outfile.close()
