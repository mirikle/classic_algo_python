passed = set([])
def backtrack(matrix, r, c, path):
    
    if (r, c) in passed: return
    passed.add((r, c))
    
    if matrix[r][c] == 'X':
        return True
    
    # top
    r -= 1
    if r > -1 and matrix[r][c] != 'w':
        path.append(1)
        if backtrack(matrix, r, c, path): return True
        path.pop()
    r += 1
    
    # right
    c += 1
    if c < len(matrix[0]) and matrix[r][c] != 'w':
        path.append(2)
        if backtrack(matrix, r, c, path): return True
        path.pop()
    c -= 1 
    
    # down
    r += 1
    if r < len(matrix) and matrix[r][c] != 'w':
        path.append(3)
        if backtrack(matrix, r, c, path): return True
        path.pop()
    r -= 1
    
    # left
    c -= 1
    if c > -1 and matrix[r][c] != 'w':
        path.append(4)
        if backtrack(matrix, r, c, path): return True
        path.pop()
    c += 1

def OtoX(matrix):
    orow = -1
    ocol = -1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'O':
                orow = i
                ocol = j
                break
        if orow != -1: break
    
    path = []
    backtrack(matrix, orow, ocol, path)
    print path
    


mp = '''.......
.......
w......
w.w.w..
....O..
..w....
...X...'''
matrix = mp.split('\n')
OtoX(matrix)
