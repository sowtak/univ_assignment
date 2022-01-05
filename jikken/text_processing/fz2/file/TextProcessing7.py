def alphabet_freq(text_list):
    d=[0]*26
    for c in ('').join(text_list).casefold():
        for i,v in enumerate('abcdefghijklmnopqrstuvwxyz'):
            if c==v:
                d[i]=d[i]+1
        
    return d

print(alphabet_freq(input().split()))
