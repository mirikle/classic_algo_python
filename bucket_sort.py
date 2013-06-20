seq = [7, 6, 4, 3, 2, 1, 0]

def bucket_sort(seq, jump = 2):
    bucket_num = max(seq) // jump + 1
    
    buckets = [[] for i in range(bucket_num)]
    for i in seq:
        bucket_idx = i / jump
        buckets[bucket_idx].append(i)
    
    seq = []
    for bucket in buckets:
        bucket.sort()
        for i in bucket:
            seq.append(i)
    
    return seq

print bucket_sort(seq, jump = 1)
        
        
