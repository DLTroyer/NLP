import nltk
#nltk.download("stopwords")
from nltk.corpus import stopwords
from textblob import TextBlob
from pathlib import Path
from textblob import TextBlob

blob = TextBlob(Path('RomeoAndJuliet.txt').read_text())


stops = stopwords.words("english")
'''
blob = TextBlob('Today is a beautiful day.')

newblob = [word for word in blob.words if word not in stops]

print(newblob)
'''

items = blob.word_counts.items()
items = [word for word in items if word[0] not in stops]

from operator import itemgetter

sorted_items = sorted(items, key=itemgetter(1), reverse=True)
#print(sorted_items)

top20 = sorted_items[:20]

#print(top20)

import pandas as pd

df = pd.DataFrame(top20, columns=['Word', 'Count'])

#print(df)

import matplotlib.pyplot as plt

axes = df.plot.bar(x='Word',y='Count', legend=False)



plt.gcf().tight_layout()

plt.show()