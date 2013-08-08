# Usage: python scriptname inputfile

import numpy as np
import pandas as pd
import csv
from sys import argv

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import cross_val_score
from sklearn import metrics
from sklearn.metrics import auc_score

script, infile = argv

data = pd.read_csv("%s" % infile)

vectorizer = CountVectorizer(ngram_range=(1,3))

speaker = np.array(data['speaker'], dtype=str)

# for line in speaker:
# 	if line == "program":
# 		line == "1"
# 	if line == "human":
# 		line == "0"

utterance = np.array(data['utterance'], dtype=str)

train = vectorizer.fit_transform(utterance)

model = LogisticRegression()

classifier = model.fit(train.toarray(), speaker)

# fpr, tpr, thresholds = metrics.roc_curve(speaker, classifier, pos_label="program")

print (cross_val_score(model, train.toarray(), speaker, cv = 10).mean())
#, score_func=auc_score