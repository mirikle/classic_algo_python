seq = [0, 0, 0, 0, 0, 1, 1, 1]

longest = -1
l_start = -1
l_end = -1
size = len(seq)
# zeros[i][j] the 0 or 1s from i to j
zeros = [[0 for j in range(size)] for i in range(size)]
ones = [[0 for i in range(size)] for j in range(size)]
for k in range(size):
    for i in range(size - k):
        if seq[i + k] == 0:
            zeros[i][i + k] = zeros[i][i + k - 1] + 1
            ones[i][i + k] = ones[i][i + k - 1]
        else:
            zeros[i][i + k] = zeros[i][i + k - 1]
            ones[i][i + k] = ones[i][i + k - 1] + 1
        if zeros[i][i + k] == ones[i][i + k]:
            if k + 1 > longest: 
                longest = k + 1
                l_start = i
                l_end = i + k
            
print '\n'.join([str(row) for row in ones])
print
print '\n'.join([str(row) for row in zeros])
print longest, l_start, l_end
                
