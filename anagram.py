sentence = "The rat fell in the tar llef"

def anagram(sentence):
    seq = sentence.split()
    anagram_keeper = {}
    for word in seq:
        lst = list(word)
        lst.sort()
        tplst = tuple(lst)
        anagram_keeper.setdefault(tplst, [])
        anagram_keeper[tplst].append(word)
    ret = []
    for words in anagram_keeper.values():
        if len(words) > 1:
            ret.append(words)
    return ret

print anagram(sentence)