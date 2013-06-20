class Node:
    def __init__(self, start, substr):
        self.start = start
        self.substr = substr
        self.branches = {}
def count_sim(substr, new_suffix):
    i = 0
    while i < len(substr):
        if substr[i] != new_suffix[i]:
            break
        i += 1
    return i
def insert_into_tree(subroot, suffix, prefix_len, start):
    prefix = str(suffix[:prefix_len])
    new_suffix = str(suffix[prefix_len:])
    if(len(subroot.branches) == 0):
        left_child = Node(subroot.start, prefix)
        right_child = Node(start, new_suffix)
        subroot.branches[prefix] = left_child
        subroot.branches[new_suffix] = right_child
    else:
        if prefix_len == len(subroot.substr):
            for substr, node in subroot.branches.items():
                if len(substr) > 0:
                    i = count_sim(substr, new_suffix)
                    if i > 0:
                        insert_into_tree(node, new_suffix, i, start)
                        break
            else:
                new_child = Node(start, new_suffix)
                subroot.branches[new_suffix] = new_child
        else:
            parent_prefix = prefix
            left_prefix = str(subroot.substr[prefix_len:])
            left = Node(subroot.start, left_prefix)
            subroot.prefix = parent_prefix
            import copy
            left.branches = copy.deepcopy(subroot.branches)
            subroot.branches = {left_prefix: left, new_suffix: Node(start, new_suffix)}

def build_suffix_tree(t_str):
    len_str = len(t_str)
    i = len_str - 1
    root = Node(len_str, "")
    while i >= 0:
        insert_into_tree(root, str(t_str[i:]), 0, i)
        i -= 1
    del root.branches[""]
    return root

def display_all_suffix(subroot, suffix_s_prefix, level = 0):
    prefix = ''.join(['->' for i in range(level)])
    if len(subroot.branches) == 0:
        print prefix + suffix_s_prefix
        return
    for substr, node in subroot.branches.items():
        display_all_suffix(node, suffix_s_prefix + substr, level + 1)
        
def display(subroot, level = 0):
    prefix = ''.join(['->' for i in range(level)])
    print prefix + str(subroot.substr)
    for substr, node in subroot.branches.items():
        display(node, level + 1)
    
#root = build_suffix_tree("BCABC")
#display_all_suffix(root, "")

c = int(raw_input())
for i in range(c):
    s = raw_input()
    root = build_suffix_tree(s)
    display(root)

    def count(subroot, test, idx, total):
        score = 0
        if test:
            for j in range(idx, idx + len(subroot.substr)):
                if s[j] == subroot.substr[j - idx]: 
                    score += 1
                else:
                    break
        cnt = 0 # how many suffices exist on this subroot, included
        test = score == len(subroot.substr)
        if len(subroot.branches) > 0:
            for substr, node in subroot.branches.items():
                cnt += count(node, test, idx + score, total)
        else:
            cnt = 1
        total[0] += cnt * score
        print subroot.substr, cnt, score
        return cnt
    
    total = [0]
    count(root, True, 0, total)
    print total[0]
