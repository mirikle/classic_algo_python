arr = [3, 4, 5, 6, 1, 2, 7, 8]
k = 5
heap = [arr[i] for i in range(k)]
heap_size = k

def down_heap(heap, cur_idx): 
	cur = cur_idx
	while 1:
		left = 2 * cur + 1
		right = 2 * cur + 2
		smallest = cur
		if left < heap_size and heap[left] < heap[smallest]: smallest = left
		if right < heap_size and heap[right] < heap[smallest]: smallest = right
		if smallest == cur: break
		heap[cur], heap[smallest] = heap[smallest], heap[cur]
		cur = smallest

def delete_heap(heap, idx):
	global heap_size
	heap_size -= 1
	heap[idx], heap[heap_size] = heap[heap_size], heap[idx]
	down_heap(heap, idx)

def top_heap(heap, cur_idx):
	while cur_idx > 0:
		parent = (cur_idx - 1) / 2
		if heap[parent] > heap[cur_idx]:
			heap[parent], heap[cur_idx] = heap[cur_idx], heap[parent]
		else: return

def insert_heap(heap, item):
	global heap_size
	heap_size += 1
	heap[heap_size - 1] = item
	top_heap(heap, heap_size - 1)

#build_heap
heap_size = k
for i in range(k / 2 - 1, -1, -1):
	down_heap(heap, i)

print heap[0]
for i in range(k, len(arr)):
	to_be_del = arr[i - k]
	del_idx = -1
	for j, item in enumerate(heap):
		if item == to_be_del: del_idx = j
	delete_heap(heap, del_idx)
	insert_heap(heap, arr[i])
	print heap[0]

