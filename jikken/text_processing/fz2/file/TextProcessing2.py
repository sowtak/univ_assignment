def three_letter_words(list_words):
    return sorted(list(set([w.casefold() for w in list_words if len(w)==3])))

print(three_letter_words(input().split()))
