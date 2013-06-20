seq = [-4, -2, 1, 2, 3, 4, 6, 7, 8, 2, 3, 4, 5, 6, 7]

start = [0 for i in range(len(seq))]
for i in range(1, len(seq)):
    if seq[i] > seq[i - 1]:
        start[i] = start[i - 1]
    else:
        start[i] = i
max_len = -2 ** 31
for i in range(len(seq)):
    if i - start[i] + 1 >= max_len:
        max_len = i - start[i] + 1

print max_len
