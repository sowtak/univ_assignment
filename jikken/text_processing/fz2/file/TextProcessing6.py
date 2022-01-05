import re
def count_words(seq_words):
    return len(set([w.casefold() for w in re.split(r'\s|[.,]',seq_words) if w != '']))

print(count_words(input()))


