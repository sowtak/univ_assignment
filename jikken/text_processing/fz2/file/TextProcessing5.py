def file_to_list(filename):
    ret=[]
    f=open(filename, 'r')
    for line in f:
        line=line.strip()
        line=line.replace('-',' ')
        words=line.split(' ')
        for w in words:
            for delim in [',', '.',';',':','\'','\"', '?', '!', '0' '1' '2' '3' '4' '5' '6' '7' '8' '9']:
                w=w.replace(delim,'')
            if w != '':
                ret.append(w)
    return ret

print(file_to_list(input()))
            
                 

