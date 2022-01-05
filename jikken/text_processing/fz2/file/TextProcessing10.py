def palindrome_j(text):
    punc=''
    if text[len(text)-1]=='。':
        punc='。'
        text=text[:-1]
    
    text_rev=text[::-1]
    if punc != '':
        text_rev+=punc
    
    return text_rev

print(palindrome_j(input()))
