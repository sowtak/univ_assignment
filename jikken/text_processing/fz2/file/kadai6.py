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
    
    ret={}
    for e in nouns_dict:
        for v in vals:
            if v == nouns_dict[e]:
                ret.update({e:nouns_dict[e]})

    return ret

f=open(os.path.join(sys.path[0], "wagahaiwa_nekodearu.txt"), "r", encoding='shift_jis')
print(top30_jnoun(f))
f.close()
