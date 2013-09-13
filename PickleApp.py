import pickle
import scipy.sparse
import numpy as np
# import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

classifier = pickle.load(open("save.p", "rb"))

vectorizer = pickle.load(open("save2.p", "rb"))

userinput = raw_input("How are you doing today? ")

length = len(userinput.split())

userinput = "<start> " + userinput + " <end>"

train1 = vectorizer.transform([userinput])

final = scipy.sparse.hstack( (train1, length ))

# userinput = userinput.toarray()

# userinput2 = raw_input("What do you think of the Turing Test? ")

# userinput2 = "<start> " + userinput2

# userinput = np.array(userinput, userinput2, dtype=str)

# vectorizer = CountVectorizer(strip_accents='unicode', ngram_range=(1,2))


close = classifier.predict_proba(final.toarray())

print close[:,1:]