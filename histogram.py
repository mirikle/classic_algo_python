heights = [7, 2, 1, 4, 5, 1, 3, 3]

def build_order_static_tree(heights):
    size = len(heights)
    # [value, left, right, min_idx]
    heap = [[-1, None, None, None] for i in range(2 * size)]
    i = 2 * size - 1
    j = size - 1
    while j > -1:
        heap[i][0] = heights[j]
        heap[i][1] = i - size
        heap[i][2] = i - size
        heap[i][3] = i - size
        i -= 1
        j -= 1
    # idx: the currrent index
    def build(idx):
        left = 2 * idx
        right = 2 * idx + 1
        if left > size - 1:
            heap[idx][0] = min(heap[left][0], heap[right][0])
            heap[idx][1] = heap[left][1]
            heap[idx][2] = heap[right][2]
            if heap[idx][0] == heap[left][0]: heap[idx][3] = heap[left][3]
            else: heap[idx][3] = heap[right][3]
            return heap[idx]
        lsub_heap = build(left)
        rsub_heap = build(right)
        heap[idx][0] = min(lsub_heap[0], rsub_heap[0])
        heap[idx][1] = lsub_heap[1]
        heap[idx][2] = rsub_heap[2]
        if heap[idx][0] == lsub_heap[0]: heap[idx][3] = lsub_heap[3]
        else: heap[idx][3] = rsub_heap[3]
        return heap[idx]
    build(1)
    return heap
            
'''
the return value is (min, min_idx)
'''
def min_height(heap, start, end, cur=1):
        s = heap[cur][1]
        e = heap[cur][2]
        if s == start and e == end:
            return heap[cur][0], heap[cur][3]
        else:
            left = 2 * cur
            right = left + 1
		  # the search goes to left branch require the left branch includes the [start, end] in total, the heap[left][2] is the right most value of the left branch, the same goes with the right branch
            if end <= heap[left][2]:
                return min_height(heap, start, end, left)
            if start >= heap[right][1]:
                return min_height(heap, start, end, right)
            lsub = min_height(heap, start, heap[left][2], left)
            rsub = min_height(heap, heap[right][1], end, right)
            if lsub[0] <= rsub[0]: return lsub
            else: return rsub

heap = build_order_static_tree(heights)
#print min_height(heap, 6, 7)

'''
the max area for [i, j] is
the lowest plank from i to j is k,
max( area([i, k - 1]) , area([k + 1, j]), height(k) * (j - i + 1))
'''
def largest_rectarea(start, end):
    if start > end: return -2 ** 31
    if start == end: return heights[start]
    min_val, min_idx = min_height(heap, start, end)
    left_area = largest_rectarea(start, min_idx - 1)
    right_area = largest_rectarea(min_idx + 1, end)
    idx_area = min_val * (end - start + 1)
    return max(left_area, right_area, idx_area)

print largest_rectarea(0, 7)
