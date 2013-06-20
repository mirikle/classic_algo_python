seq = list('/root//foo/bar')

def rmdupslash(seq):
    length = len(seq)
    prev = seq[0]
    i = 1
    while i < length:
        if prev == '/' and seq[i] == '/':
            for j in range(i + 1, length):
                seq[j - 1] = seq[j]
            length -= 1
        prev = seq[i]
        i += 1
    return ''.join(seq[:length])
    
print rmdupslash(seq)