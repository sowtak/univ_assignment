import re
import nltk
nltk.download('book')
from nltk.book import *

def count_words(text):
    vocs=[]
    for w in text:
        w=w.casefold()
        w=re.sub(r'[^a-z\s]','',w)
        if w not in vocs and w != '':
            vocs.append(w)
    return len(set(vocs))


for text in [text1,text2,text3,text4,text5,text6, text7, text8, text9]:
    print(count_words(text))



