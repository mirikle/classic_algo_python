class node:
    def __init__(self):
        self.letters = {}
        self.leaves = set([])

def add_word(subroot, level, word):
    if word[level] not in subroot.letters:
        subroot.letters[word[level]] = node()
    if level == len(word) - 1:
        subroot.leaves.add(word[-1])
        return
    add_word(subroot.letters[word[level]], level + 1, word)

def morder_traversal(subroot, res, results):
    for key, branch in subroot.letters.items():
        res.append(key)
        morder_traversal(branch, res, results)
        if key in subroot.leaves:
            results.append(''.join(res))
        res.pop()

def display_all_words(root):
    results = []
    morder_traversal(root, [], results)
    print results
    
def find_lcp(subroot, res):
    if len(subroot.letters) > 1:
        return
    for key in subroot.letters:
        res.append(key)
        find_lcp(subroot.letters[key], res)

def lcp(arr):
    root = node()
    for word in arr:
        add_word(root, 0, word)
    display_all_words(root)
    res = []
    find_lcp(root, res)
    print ''.join(res)
    
arr = ['abcddddddd', 'abcddddd', 'abcddddddeee', 'abeerjkjk']
lcp(arr)
        

    