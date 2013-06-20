candidates = set(["fooo", "barr", "wing", "ding", "wing"])
seq = "lingmindraboofooowingdingbarrwingmonkeypoundcake"

for i in range(4):
    j = i
    while j < len(seq):
        sub = seq[j: j + 4]
        if sub in candidates:
            mp = {sub: 1}
            k = j + 4
            while k < len(seq) - 4 and k < len(candidates) * 4 + j:
                sub = seq[k: k + 4]
                if sub in candidates and sub not in mp:
                    mp[sub] = 1
                else:
                    break
                if len(mp) == len(candidates):
                    print seq[j:k + 4]
                    break
                k += 4
        j += 4
        
