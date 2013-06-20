T = int(raw_input())
reduce_dict = {
    'ab': 'c',
    'ba': 'c',
    'ac': 'b',
    'ca': 'b',
    'bc': 'a',
    'cb': 'a'
}

def append_reduce(s, ch):
    if len(s) == 0: return ch
    if s[-1] == ch:
        return s + ch
    else:
        if len(s) % 2 == 0:
            return ch
        else:
            return reduce_dict[s[-1] + ch]

def f(s, i, j):
    if i > j: return ''
    if i == j: return s[i]
    '''
    if f_buf[i][j] != -1:
        print 'SHOT: i[%d], j[%d]' % (i, j)
    '''
    if f_buf[i][j] == -1: 
        min_len = [10**8]
        min_remain = ['']
        for k in range(i, j + 1):
            s1 = f(s, i, k - 1)
            s2 = f(s, k + 1, j)
            # update_min_remain: reduce the merged string sp1, sp2
            #         and update min
            def update_min_remain(sp1, sp2, min_len, min_remain):
                if len(sp1) == 0 or len(sp2) == 0:
                    ss = sp1 + sp2
                else:
                    if sp1[-1] != sp2[0]:
                        if len(sp2) % 2 == 0:
                            ss = sp1
                        else:
                            ch = reduce_dict[sp1[-1] + sp2[0]]
                            sp1 = sp1[:-1]
                            ss = append_reduce(sp1, ch)
                    else:
                        ss = sp1 + sp2
                #print 'SP1[%s], SP2[%s], SS[%s]' % (sp1, sp2, ss)
                tmp_len = len(ss)
                if tmp_len <  min_len[0]:
                    min_len[0] = tmp_len
                    min_remain[0] = ss

            # 1. merge to left first
            s11 = append_reduce(s1, s[k])
            update_min_remain(s11, s2, min_len, min_remain)
            # 2. merge to right first
            s22 = append_reduce(s2, s[k])
            update_min_remain(s1, s22, min_len, min_remain)
            #print 'i[%d], j[%d], k[%d], s1[%s], s2[%s], min_remain[%s]' % (i, j, k, s1, s2, min_remain[0])
        f_buf[i][j] = min_remain[0]
    return f_buf[i][j]

for i in range(T):
    s = list(raw_input())
    size = len(s)
    f_buf = [ [-1] * size for i in range(size)]  
    ret = f(s, 0, size - 1)
    #print ret
    print len(ret)
