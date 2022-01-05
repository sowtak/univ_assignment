import MeCab
import os
import sys

m=MeCab.Tagger('-Ochasen')
m.parse('')

def top30_jnoun(text):
    result=m.parse(text.read())
    lines=result.split('\n')
    nouns_dict={}
    for line in lines:
        feature=line.split('\t')
        if len(feature) >= 4:
            if "名詞" in feature[3]:
                if feature[0] not in nouns_dict:
                    nouns_dict[feature[0]]=1
                else:
                    nouns_dict[feature[0]]+=1
    
    
    vals=list(sorted(list(nouns_dict.values()), reverse=True))[:30]
    
    ret=[]
    for e in nouns_dict:
        for v in vals:
            if v == nouns_dict[e]:
                ret.append(e)

    return list(set(ret))

f=open(os.path.join(sys.path[0], "wagahaiwa_nekodearu.txt"), "r", encoding='shift_jis')
t30j=top30_jnoun(f)
f.close()
f=open(os.path.join(sys.path[0], "wagahaiwa_nekodearu.txt"), "r", encoding='shift_jis')
word_list=[]
lines=m.parse(f.read()).split('\n')
num_words=len(lines)
for line in lines:
    feat=line.split('\t')
    if len(feat)>=4:
        word_list.append(feat[0])

f.close()

def percent_jword(text, word):
    num_t30j_words=0
    for w in word:
        if w in text:
            num_t30j_words+=1

    return num_t30j_words/num_words


print(percent_jword(t30j, word_list))
