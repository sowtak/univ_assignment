import re
import collections
import nltk
nltk.download('book')
from nltk.book import *

def top_n_words(text, n):
    d={}
    for w in text:
        w=w.lower()
        if len(w)>=4:
            if w not in d:
                d[w]=1
            else:
                d[w]=d[w]+1
    ret={}
    ret=dict(collections.Counter(d).most_common(n))
    return ret


texts=[text1,text2,text3,text4,text5,text6, text7, text8, text9]

for text in texts:
    print(top_n_words(text, 5))

print()
whole_text=[]
for text in texts:
    whole_text+=text.tokens

print(top_n_words(whole_text, 1))


