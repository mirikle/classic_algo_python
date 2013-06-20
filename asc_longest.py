from copy import deepcopy 

def longest_common_substr(str1, str2, m, n, mp):
    if m < 0 or n < 0:
        return []
    
    if (m, n) in mp:
        return mp[(m, n)]
    
    result = None
    if str1[m] == str2[n]:
        result = longest_common_substr(str1, str2, m - 1, n - 1, mp) + [str1[m]]
    else:
        str_tmp1 = longest_common_substr(str1, str2, m - 1, n, mp)
        str_tmp2 = longest_common_substr(str1, str2, m, n - 1, mp)
        if len(str_tmp1) > len(str_tmp2):
            result = str_tmp1
        else:
            result = str_tmp2
    
    mp[(m, n)] = result
    return result

'''
O(n^2)
'''
def longest_ascending_seq(seq):
    seq2 = deepcopy(seq)
    seq2.sort()
    return longest_common_substr(seq, seq2, len(seq) - 1, len(seq) - 1, {})

seq = [1, 2, 3, 8, 10, 5, 6, 7, 12, 9, 4, 0]
print longest_ascending_seq(seq)
