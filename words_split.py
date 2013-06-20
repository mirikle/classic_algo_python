words = ['spare', 'man', 'manipulate', 'great']

def build_trie(words):
	# if a node is word, then the index pointing it is last letter of that word
	class node:
		def __init__(self, is_word):
			self.is_word = is_word
			self.branches = {}
			
	def insert_into_trie(subroot, cur_idx, word):
		ch = word[cur_idx]
		is_word = False if cur_idx < (len(word) - 1) else True
		cur_node = None
		if ch in subroot.branches: 
			cur_node = subroot.branches[ch]
			if is_word: cur_node.is_word = True
		else:
			cur_node = node(is_word)
			subroot.branches[ch] = cur_node
		if is_word: return
		insert_into_trie(cur_node, cur_idx + 1, word)

	root = node(False)
	for word in words:
		insert_into_trie(root, 0, word)

	return root

def print_trie(root):
	def print_sub(subroot, prefix):
		if subroot.is_word:
			print ''.join(prefix)
		for ch in subroot.branches:
			prefix.append(ch)
			print_sub(subroot.branches[ch], prefix)
			prefix.pop()

	print_sub(root, [])

trie = build_trie(words)
print_trie(trie)

# 2 exist, and has branches
# 1 exist, no branches
# -1 not a word, but has branches (match till now)
# 0 not match
def check_word(trie, word):
	def check(subroot, cur_idx, word):
		if cur_idx == len(word):
			if subroot.is_word:
				if len(subroot.branches) == 0:	
					return 1
				else:
					return 2
			else:
				return -1
		if word[cur_idx] in subroot.branches:
			return check(subroot.branches[word[cur_idx]], cur_idx + 1, word)
		else:
			return 0
	return check(trie, 0, word)

print check_word(trie, 'man')
print check_word(trie, 'manipulate')
print check_word(trie, 'manipxulate')
print check_word(trie, 'gr')

def split_words(sentence):
	print 'Splitting: ', sentence
	eligible = -1 
	prev = -1
	cur_word = ''
	i = 0
	while i < len(sentence):
		ch = sentence[i]
		cur_word += ch
		ret = check_word(trie, cur_word)
		if ret == 1: 
			print cur_word
			cur_word = ''
			prev = i
		elif ret == 2: #check for longer ones
			eligible = i
		elif ret == 0:
			if eligible <= prev:
				print 'FAILURE!'
				return
			else:
				print ''.join(sentence[prev + 1 : eligible + 1])
				i = eligible
				prev = i
				cur_word = ''
		i += 1

split_words('manipxulatesparegreat')
split_words('manipulatesparegreat')
