def partition(arr, s, e):
    pivot = arr[(s + e) / 2]
    while s <= e:
        while arr[s] < pivot: s += 1
        while arr[e] > pivot: e -= 1
        if s <= e: 
            arr[s], arr[e] = arr[e], arr[s]
            s += 1
            e -= 1
    return s

#arr = [1, 2 , 3]
#print partition2(arr, 0, 2)
#print arr

#arr = [5, 5]
#partition(arr, 0, 1)

def quick_sort(arr, s, e):
    p_idx = partition(arr, s, e)
    if s < p_idx - 1:
        quick_sort(arr, s, p_idx - 1)
    if e > p_idx:
        quick_sort(arr, p_idx, e)
    
arr = [5, 5, 5, 3, 5, 5, 5]
quick_sort(arr, 0, len(arr) - 1)
print arr

def partition2(arr, s, e):
    pivot = arr[s]
    while s < e:
        while arr[e] > pivot and e > s: e -= 1
        arr[s] = arr[e]
        while arr[s] <= pivot and s < e: s += 1
        arr[e] = arr[s]
    arr[s] = pivot
    return s

def quick_sort2(arr, s, e):
    if s < e:
        k = partition2(arr, s, e)
        quick_sort2(arr, s, k - 1)
        quick_sort2(arr, k + 1, e)
    
arr = [5, 5, 5, 3, 5, 5, 5]
quick_sort2(arr, 0, len(arr) - 1)
print arr

arr = [1, 2]
partition2(arr, 0, 1)
print arr;