def longest_common_substr(str1, str2, m, n, mp):
    if m < 0 or n < 0:
        return ''
    
    if (m, n) in mp:
        return mp[(m, n)]
    
    result = ''
    if str1[m] == str2[n]:
        result = longest_common_substr(str1, str2, m - 1, n - 1, mp) + str1[m]
    else:
        str_tmp1 = longest_common_substr(str1, str2, m - 1, n, mp)
        str_tmp2 = longest_common_substr(str1, str2, m, n - 1, mp)
        if len(str_tmp1) > len(str_tmp2):
            result = str_tmp1
        else:
            result = str_tmp2
    
    mp[(m, n)] = result
    return result

seq1 = 'abcdalasjdflasjdlkfjasklfjqwejroiwjklasjdflajsdlfjals;dfkjasl;dfjkalsdfjasldffefg'
seq2 = 'aebcdgasdfjkljw2eojklasjfalksdjfklasdfjlasdfasdfaskldfjlaksjdflaksjdfklajsdflkajsldfjalsdfjaskdfjaskdfj'
print longest_common_substr(seq1, seq2, len(seq1) - 1, len(seq2) - 1, {})