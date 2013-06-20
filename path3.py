mp = '''.......
.......
w......
w.w.w..
....O..
..www..
...X...'''

matrix = mp.split('\n')
visited = [[False for j in range(len(matrix[0]))] for i in range(len(matrix))]
xrow = 6
xcol = 3
dr = [0, 0, 1, -1] #, -1, 1, -1, 1]
dc = [1, -1, 0, 0] #, -1, 1, 1, -1]

def backtrack(r, c, path):
    visited[r][c] = True
    if matrix[r][c] == 'X':
        return True
    
    newpos = []
    for i in range(len(dr)):
        newr = r + dr[i]
        newc = c + dc[i]
        # note the contraints here
        if 0 <= newr < len(matrix[0]) and 0 <= newc < len(matrix[0])\
         and matrix[newr][newc] != 'w' and not visited[newr][newc]:
            newpos.append((newr, newc, i))
    
    # the evaluation function, euclidian distance
    lst = []
    for item in newpos:
        distsq = (item[0] - xrow) ** 2 + (item[1] - xcol) ** 2
        lst.append((distsq, item))
    lst.sort()
    
    # from the nearest point to the farthest
    for it in lst:
        item = it[1]
        path.append(item[2])
        if backtrack(item[0], item[1], path): return True
        path.pop()

path = []
backtrack(4, 4, path)
print path


    

