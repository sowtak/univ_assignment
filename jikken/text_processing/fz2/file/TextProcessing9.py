import re
def vocabulary(seq_words):
    return [w.casefold() for w in re.split(r'\s|[.,]',seq_words) if w != '']

def word_radio(word_list1, word_list2):
    voc_list1=vocabulary(word_list1)
    num_voc1=len(voc_list1)
    if num_voc1==0:
        return 0

    matches=0
    for w in word_list2.split():
        w=w.casefold()
        for voc1 in voc_list1:
            if w==voc1:
                matches=matches+1

    return matches/num_voc1
    

print(word_radio(input(),input()))
