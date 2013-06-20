def atoi(stri):
    head = -1
    pw = 1
    if stri[0] == '-':
        head = 0
        pw = -1
    rt = 0
    for i in range(len(stri) - 1, head, -1):
        ch = stri[i]
        if '0' <= ch <= '9':
            rt += pw * int(ch)
        else:
            raise Exception('unexpected format!')
        pw *= 10
    return rt

print(atoi('-00012340'))