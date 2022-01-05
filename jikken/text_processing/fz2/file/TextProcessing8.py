def top_ten_words(list_text):
    d={}
    for w in list_text:
        w=w.casefold()
        if len(w)>=4:
            if w not in d:
                d[w]=1
            else:
                d[w]+=1
 
    vals=list(sorted(list(d.values()), reverse=True))[:10]
    
    ret={}
    for e in d:
        for v in vals:
            if v == d[e]:
                ret.update({e:d[e]})

    return ret
                
print(top_ten_words(input().split()))

