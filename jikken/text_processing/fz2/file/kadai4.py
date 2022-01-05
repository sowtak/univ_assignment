import re
import collections
import nltk
nltk.download('book')
from nltk.book import *
from nltk.corpus import stopwords

def stopwords_wordcount_ratio(text):
    _stopwords=stopwords.words('english')
    stopwords_count=0
    for w in text:
        for stopword in _stopwords:
            if w==stopword:
                stopwords_count+=1
                continue
    
    return stopwords_count/len(text.tokens)


texts=[text1,text2,text3,text4,text5,text6, text7, text8, text9]

for text in texts:
    print(stopwords_wordcount_ratio(text))



