matrix = [[0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0]]

def max_zero_sub_matrix(matrix):
    col_size = len(matrix[0])
    row_size = len(matrix)
    
    h_matrix = [[0 for i in range(col_size)] for j in range(row_size)]
    
    for i in range(col_size): 
        if matrix[0][i] == 0: h_matrix[0][i] = 1 
    for i in range(1, row_size):
        for j in range(col_size):
            if matrix[i][j] == 0: h_matrix[i][j] = h_matrix[i - 1][j] + 1
            
    max_zeros = -2 ** 31
    bottom = -1
    left = -1
    right = -1
    for i in range(row_size):
        l_bound = [k for k in range(col_size)]
        r_bound = [k for k in range(col_size)]
        
        for j in range(col_size):
            while l_bound[j] > 0 and h_matrix[i][j] <= h_matrix[i][l_bound[j] - 1]:
                # this can make the decreasing of the index faster
                # suppose that j = 4, now l_bound[3] already reaches 0, so only one step
                # l_bound[4] reaches 0, no need to decrease one by one, although that's 
                # also correct
                l_bound[j] = l_bound[l_bound[j] - 1]
        for j in range(col_size - 1, -1, -1):
            while r_bound[j] < col_size - 1 and h_matrix[i][j] <= h_matrix[i][r_bound[j] + 1]:
                r_bound[j] = r_bound[r_bound[j] + 1]
            
        for j in range(col_size):
            area = h_matrix[i][j] * (r_bound[j] - l_bound[j] + 1)
            if area > max_zeros:
                max_zeros = area
                bottom = i
                left = l_bound[j]
                right = r_bound[j]
                
    return max_zeros, bottom, left, right
     
print max_zero_sub_matrix(matrix)
