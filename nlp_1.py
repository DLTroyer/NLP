from textblob import TextBlob

text = "Today is"

blob = TextBlob(text)

#print(blob.sentences)

#print(blob.words)

#print(blob.tags)

#print(blob.noun_phrases)

#scale from -1 to 1
#subjectivity: high = more subjectivity
#polarity: + = positive, - = negative
print(blob.sentiment)

print(round(blob.sentiment.polarity,3))
print(round(blob.sentiment.subjectivity,3))

'''
sentences = blob.sentences

for sentence in sentences:
    print(sentence)
    print(sentence.sentiment)
    print(round(sentence.sentiment.polarity,3))
    print(round(sentence.sentiment.subjectivity,3))
'''

from textblob.sentiment import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer=NaiveBayerAnalyser())

#print(blob.sentiment)

sentences = blob.sentences

#for sentence in sentences:
    #print(sentence.sentiment)

print(blob.detect_language())

spanish = blob.translate(to='es')

print(spanish)

from textblob import Word

index = Word('index')

print(index.pluralize())

animals = TextBlob('dog cat fish sheep bird').words

print(animals.pluralize())

cacti = Word('cacti')

print(cacti.singularize())

word = Word('theyr')

#returns the possible solutions and the percentage that they recomend which option
print(word.spellcheck())

word.correct()

print(word)

sentence = TextBlob('Ths sentense has missplled wrds.')

sentence = sentence.correct()

print(sentence)
