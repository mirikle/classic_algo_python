def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    print tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r - 1)):
            cycles[i] -= 1
            if cycles[i] == 0:
                # when the ith bit of cycles is zero, 
                # move the ith element of the indices to the end
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                print tuple(pool[i] for i in indices[:r])
                break
        else:
            return
permutations(tuple([7, 8, 9]))
