'''
Terseness doen't cover the stupidness of this solution. yes it is!!! but now I know the better way now which gives O(n^2)

arr[i] = longest(arr[j] + 1) for all j < i and seq[j] < seq[i]
'''

#seq = [2, 1, 3, 2, 3, 4, 1, 5, 2, 3, 4, 6, 7]
seq = [1, 2, 3, 8, 10, 5, 6, 7, 12, 9, 4, 0]

def longest_asc_seq(seq):
    cands = [[seq[0]]]
    for i in range(1, len(seq)):
        llen = -1
        llast = None
        for cand in cands:
            if cand[-1] < seq[i]:
                cands.append(cand + [seq[i]])
            if len(cand) > llen:
                llen = len(cand)
                llast = cand[-1]
        cands.append([seq[i]])
        cands = filter(lambda cand: len(cand) == llen or cand[-1] < llast, cands)
    
    maxlen = -1
    for i in cands:
        if len(i) > maxlen:
            maxlen = len(i)
    return filter(lambda cand : len(cand) == maxlen, cands)

print longest_asc_seq(seq) 
                


            
