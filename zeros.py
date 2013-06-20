def zerosets(arr):
    tb_counter = {}
    for i, a in enumerate(arr):
        tb_counter.setdefault(a, [])
        tb_counter[a].append(i)
    
    result = []
    used = set([])
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            want = - (arr[i] + arr[j])
            if want in tb_counter.keys():
                avail = tb_counter[want]
                for k in avail:
                    if k != i and k != j:
                        condidate = [i, j, k]
                        condidate.sort()
                        candidate = tuple(condidate)
                        if candidate not in used:
                            used.add(candidate)
                            result.append((arr[i], arr[j], arr[k]))
    return result

print zerosets([0, 0, 0, 0, -1, 1]) 
