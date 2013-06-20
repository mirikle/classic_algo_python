seq = [1, 1, 2, 2, 0, 0, 1, 2, 0]

buckets = [0, 0, 0]
for i in seq:
    buckets[i] += 1

seq = []
for i in range(len(buckets)):
    for l in range(buckets[i]):
        seq.append(i)

print seq
    
