passed = set([])
def backtrack(matrix, r, c, path, xrow, xcol):
    
    if (r, c) in passed: return
    passed.add((r, c))
    
    if matrix[r][c] == 'X':
        return True
    
    cand = []
    # top
    if r > 0 and matrix[r - 1][c] != 'w': 
        cand.append(((r - 1, c), 1))
    # right
    if c < len(matrix[0]) - 1 and matrix[r][c + 1] != 'w': 
        cand.append(((r, c + 1), 2))
    # down
    if r < len(matrix) - 1 and matrix[r + 1][c] != 'w': 
        cand.append(((r + 1, c), 3))
    # left
    if c > 0 and matrix[r][c - 1] != 'w': 
        cand.append(((r, c - 1), 4))
    
    # the evaluation function, euclidian distance
    lst = []
    for item in cand:
        distsq = (item[0][0] - xrow) ** 2 + (item[0][1] - xcol) ** 2
        lst.append((distsq, item))
    lst.sort()
    
    for it in lst:
        item = it[1]
        path.append(item[1])
        if backtrack(matrix, item[0][0], item[0][1], path, xrow, xcol): return True
        path.pop()

    
def OtoX(matrix, orow, ocol, xrow, xcol):
    path = []
    backtrack(matrix, orow, ocol, path, xrow, xcol)
    print path

mp = '''.......
.......
w......
w.w.w..
....O..
..www..
...X...'''
matrix = mp.split('\n')
OtoX(matrix, 4, 4, 6, 3)
