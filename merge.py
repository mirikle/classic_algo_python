def merge(arr, s1, e1, e2):
    i = s1
    j = e1
    while i < j and j < e2:
        if arr[i] > arr[j]:
            old_j = j
            j += 1
            while j < e2 and arr[i] > arr[j]: j += 1
            exchange(arr, i, old_j, j)
        else:
            i += 1

def merge_sort(arr, s, e):
    if s == e:
        return
    m = (s + e) / 2
    merge_sort(arr, s, m)
    merge_sort(arr, m + 1, e)
    merge(arr, s, m + 1, e + 1)

def reverse(arr, start, end):
    sz = end - 1
    i = start
    while i < sz: 
        arr[sz], arr[i] = arr[i], arr[sz]
        i += 1
        sz -= 1
    return arr

def exchange(arr, start, end1, end2):
    reverse(arr, start, end1)
    reverse(arr, end1, end2)
    reverse(arr, start, end2)

#def merge0(arr, s1, e1, e2):
#    new = []
#    i = s1
#    j = e1
#    while i < e1 and j < e2:
#        if arr[i] <= arr[j]:
#            new.append(arr[i])
#            i += 1
#        else:
#            new.append(arr[j])
#            j += 1
#            
#    if i == e1:
#        for k in range(j, e2):
#            new.append(arr[k])
#    elif j == e2:
#        for k in range(i, e1):
#            new.append(arr[k])
#                
#    return new

#arr = [2, 9, 8, 1, 1.5, 7]
#merge(arr, 0, 3, 6)
#merge_sort(arr, 0, len(arr) - 1)
#print arr
#print merge0(arr, 0, 3, 6)


def merge2(arr, s1, e1, e2, e3):
    e = e2
    while e1 < e: # e1 will never cross its own border, let the left seg2 goes to the next while, starts from line 73
        if arr[e1] <= arr[e2]:
            arr[s1] = arr[e1]
            e1 += 1
        else:
            arr[s1] = arr[e2]
            e2 += 1
        s1 += 1
    while e2 < e3:
        arr[s1] = arr[e2]
        e2 += 1
        s1 += 1 
    return arr[0: e]

arr = [-1, -1, -1, 1, 2, 3, -1, 5, 6]
print arr
print merge2(arr, 0, 3, 6, 9)
