'''
heap sort is totally in-place
'''
def maxheapify(arr, length, i):
    cur = i
    while cur < length:
        left = 2 * cur
        right = 2 * cur + 1
        
        largest = cur
        if left < length and arr[largest] < arr[left]: 
            largest = left
        if right < length and arr[largest] < arr[right]:
            largest = right
        if largest == cur: break
        
        arr[cur], arr[largest] = arr[largest], arr[cur]
        cur = largest
        
def buildmaxheap(arr, length):
    for i in range(length / 2 - 1, -1, -1):
        maxheapify(arr, length, i)

def heapsort(arr):
    buildmaxheap(arr, len(arr))
    for i in range(len(arr) - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        maxheapify(arr, i, 0)

arr = [2, 1, 3, 7, 4]
heapsort(arr)
print arr