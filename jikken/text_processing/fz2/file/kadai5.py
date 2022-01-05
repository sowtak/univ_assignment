import MeCab
import os
import sys
m=MeCab.Tagger('-Ochasen')
m.parse('')

def percent_noun(text):
    result=m.parse(text.read())
    lines=result.split('\n')
    nouns=0
    parts=0
    for line in lines:
        feature=line.split('\t')
        if len(feature) >= 4:
            if "名詞" in feature[3]:
                nouns+=1 
        parts+=1
    
    return nouns/parts

f=open(os.path.join(sys.path[0], "wagahaiwa_nekodearu.txt"), "r", encoding='shift_jis')
print(percent_noun(f))
f.close()
