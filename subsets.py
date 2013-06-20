seq = [1, 2, 3, 4]

def subsets(seq, s, e):
    if s == e:
        return [[], [seq[s]]]
    ret = []
    ss = subsets(seq, s + 1, e)
    #seq[s] not included
    ret.extend(ss)
    #include
    for s_right in ss:
        ret.append([seq[s]] + s_right)
    return ret

print subsets(seq, 0, 3)
    
