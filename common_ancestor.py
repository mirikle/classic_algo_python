class Node:
	def __init__(self, val, left = None, right = None):
		self.val, self.left, self.right = val, left, right
	def __repr__(self):
		return str(self.val)

def find_path(subroot, val, path):
	if(subroot.val == val):
		return True
	tmp = [subroot.left, subroot.right]
	for child in tmp:
		if(child):
			path.append(child)
			ret = find_path(child, val, path)
			if ret: return True
			else: path.pop()
	return False

def find_common_ancestor(subroot, val1, val2):
	status = 0
	if subroot == None: return status
	if subroot.val == val1: return 1
	if subroot.val == val2: return 2
	status = find_common_ancestor(subroot.left, val1, val2) | find_common_ancestor(subroot.right, val1, val2)
	if(status == 3): print subroot.val
	return status

root = Node(1, Node(2, Node(3), Node(4)), Node(5, Node(6), Node(7)))
path = [root]
print find_path(root, 4, path)
print path

path = [root]
print find_path(root, 6, path)
print path

print '=============='
find_common_ancestor(root, 3, 4)
