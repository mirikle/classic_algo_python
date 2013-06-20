def max_sub(arr):
    s = 0
    mx = -1
    for i in range(len(arr)):
        if s > 0:
            s += arr[i]
            if s > mx: mx = s
        else:
            s = arr[i]
    return mx

print max_sub([-1, 2, 3, -1, 2])