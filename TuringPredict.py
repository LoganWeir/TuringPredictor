
# Usage: python scriptname inputfile outputfile

import numpy as np
import pandas as pd
import csv
from sys import argv
import pickle
import scipy.sparse

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import cross_val_score

script, infile, outfile = argv
#outfile

data = pd.read_csv("%s" % infile)

vectorizer = CountVectorizer(ngram_range=(1,2), token_pattern=r'\b\w+\b')

# strip_accents='unicode', 
#token_pattern=u'(?u)\b\w\w+\b'

speaker = np.array(data['speaker'], dtype=str)

speaker = [1 if x == 'human' else 0 for x in speaker]

speaker = np.array(speaker)

utterance = np.array(data['utterance'], dtype=str)

train = vectorizer.fit_transform(utterance)

length = np.array(data['length']).reshape(-1,1)

final = scipy.sparse.hstack( (train, length ))

model = LogisticRegression(class_weight={1:0.3908, 0:0.6092})
#With tokencombinedtext: class_weight={1:0.405, 0:0.595}

classifier = model.fit(final.toarray(), speaker)

print (cross_val_score(model, final.toarray(), speaker, cv = 3).mean())

pickle.dump(classifier, open("save.p","wb"))

pickle.dump(vectorizer, open("save2.p","wb"))

coefs = sorted(zip(classifier.coef_.T , vectorizer.get_feature_names()))

outfile = open(outfile, 'w')

writer = csv.writer(outfile)

for coef, name in coefs:
	writer.writerow([name, coef])

outfile.close()
