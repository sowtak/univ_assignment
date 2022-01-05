def contain_alphabet(list_words, alphabet):
    return sorted(list(set([w.casefold() for w in list_words if alphabet.casefold() in w.casefold()])))

print(contain_alphabet(input().split(','), input()))
