import sys
sys.setrecursionlimit(100000000)
n, k = map(int, raw_input().split())
vals = []
for i in range(n):
    vals.append(int(raw_input()))

mx_profit = [ [-1 for i in range(k)] for j in range(n)]

def max_profit(level, tail_len):
    if level < 0:   return 0
    if mx_profit[level][tail_len] != -1:
        return mx_profit[level][tail_len]
    '''
    max(
        max_profit(level - 1, tail_len+1) + level
        max_profit(level -2, tail_len+2) + level-1 + level
        ...
        max_profit(level - (k - tail_len), tail_len + k-tail_len) + level-(k - tail_len)+1 + ... + level-1 + level
    )
    '''
    mx = -1
    aggr = 0
    for i in range(level - 1, max( -2, level - (k - tail_len) - 1), -1):
        aggr += vals[i + 1]
        new_tail = tail_len + (level - i)
        if new_tail == k:
            tmp = max_profit(i - 1, 0) + aggr
        else:
            tmp = max_profit(i, new_tail)  + aggr
        if tmp > mx: mx = tmp
    mx_profit[level][tail_len] = mx
    return mx



print max_profit(n - 1, 0)
