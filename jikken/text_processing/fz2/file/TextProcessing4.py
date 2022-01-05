def palindrome(text):
    symbol=''
    n=len(text)
    if text[n-1]=='.':
        symbol='.'
    elif text[n-1] == '?':
        symbol='?'
    elif text[n-1]== '!':
        symbol='!'

    l = [w.casefold() for w in text.split(' ')]
    l.reverse()
    l[0]=l[0].replace(symbol, '')
    
    ret=[]
    for i in range(len(l)):
        if l[i]=='i':
            l[i]='I'
            
        new_str=list(reversed(l[i]))
        ret.append(''.join(new_str))
    
    ret[0] = ret[0].capitalize() 
    ret[len(ret)-1] = ret[len(ret)-1]+symbol
    return (' ').join(ret)

print(palindrome(input()))
    
