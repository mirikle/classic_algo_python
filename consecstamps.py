import copy
import sys

# the possible maximum upper bound
MAX_BOUND = 1024

allowed_denomination = 5 
allowed_number = 4

upper_bound = -1
best_stamps = None

# when the maximum denomination is 1 
cur_bound = 1 * allowed_number
cur_stamps = [1]

# least_stamps[i] represents the minimum number of stamps that can derive i
least_stamps = [sys.maxint for i in range(MAX_BOUND)] 
for i in range(allowed_number + 1): least_stamps[i] = i

'''
backtrack(level) means [0, ..., level - 1] all are done, level denominations are 
selected
'''
def backtrack(level):
    global best_stamps, upper_bound, cur_stamps, cur_bound, least_stamps
    
    # reach the leave, one solution is found
    if level == allowed_denomination:
        if cur_bound > upper_bound:
            best_stamps = copy.deepcopy(cur_stamps)
            upper_bound = cur_bound
        return
    
    cur_bound_bk = cur_bound
    least_stamps_bk = copy.deepcopy(least_stamps)
    
    for deno_cand in range(cur_stamps[level - 1] + 1, cur_bound + 2):
        cur_stamps.append(deno_cand)
        ''' update the constructable integers '''
        # from 0 to the last_stamp * allowed_number
        for postage in range(cur_stamps[-2] * allowed_number):
            for possible_num in range(1, allowed_number - least_stamps[postage] + 1):
                nxtstage = postage + deno_cand * possible_num
                if nxtstage < MAX_BOUND and least_stamps[nxtstage] > least_stamps[postage] + possible_num:
                    least_stamps[nxtstage] = least_stamps[postage] + possible_num       
        '''
        using the constructable integers to update the current bound
        only when it's consecutive can this cur_bound increase
        '''
        while least_stamps[cur_bound] != sys.maxint:
            cur_bound += 1
        
        backtrack(level + 1)
        
        cur_stamps.pop()
        cur_bound = cur_bound_bk
        least_stamps = copy.deepcopy(least_stamps_bk)

backtrack(1)
print upper_bound - 1
print best_stamps