import re
import nltk
nltk.download('book')
from nltk.book import *

def alphabet_freq(text):
    d=[0]*26
    for word in text:
        word=word.casefold()
        for i,v in enumerate('abcdefghijklmnopqrstuvwxyz'):
            for w in word:
                if w==v:
                    d[i]=d[i]+1
                    continue
        
    return d

for text in [text1,text2,text3,text4,text5,text6, text7, text8, text9]:
    print(alphabet_freq(text))   
        


