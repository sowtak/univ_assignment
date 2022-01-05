import re

def find_pattern(seq_words, chrs):
    return sorted(list(set([w for w in seq_words if re.search(chrs, w) != None])))

print(find_pattern(input().split(','), input()))
