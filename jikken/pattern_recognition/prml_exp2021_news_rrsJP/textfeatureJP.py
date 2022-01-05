#coding:utf-8
from numpy import *
import MeCab
from operator import *
import codecs
import re

def get_matrix(file_name):
    tagger = MeCab.Tagger()

    allwords={}
    articlewords=[]
    titles=[]
    art_no=0
    f = codecs.open(file_name, 'r', 'utf-8')
    line=f.readline()
    while line:
        articlewords.append({})
        titles.append(re.split('\|',line)[0])
        encoded_text = line.encode('utf-8')
        node = tagger.parseToNode(encoded_text).next
        words=[]
        while node:
            if node.feature.split(",")[0] == "名詞":
                words.append(node.surface.decode('utf-8'))
            node = node.next
        for word in words:
            allwords.setdefault(word,0)
            allwords[word]+=1
            articlewords[art_no].setdefault(word,0)
            articlewords[art_no][word]+=1;
        line=f.readline()
        art_no+=1
    f.close
    wordvec=[]
    for w,c in allwords.items():
         if c>1 and len(w)>1:
            wordvec.append(w)
    return titles,wordvec,matrix([[(word in f and f[word] or 0) for word in wordvec] for f in articlewords])

def analyze_nmf_result(U,V,titles,wordvec,result_file='result.txt'):
    out_file=codecs.open(result_file, 'w', 'utf-8')
    dim,column_dim=shape(V)
    row_dim=len(titles)

    for i in range(dim):
        words=[]
        for j in range(column_dim):
            words.append((wordvec[j],V[i,j]))
        out_file.write('[')
        for s in sorted(words,key=itemgetter(1),reverse=True)[0:6]:
            out_file.write(s[0]+' ')
        out_file.write(']\n')

        articles=[]
        for j in range(row_dim):
            articles.append((titles[j],U[j,i]))
        for art in sorted(articles,key=itemgetter(1),reverse=True)[0:3]:
            out_file.write(art[0]+' '+str(art[1])+'\n')
        out_file.write('\n')

    out_file.close()
    return


