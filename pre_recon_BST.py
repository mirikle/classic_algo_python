class Node:
	def __init__(self, val, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

def reconstruct_bst(arr):
	root = Node(arr[0])
	stk = [root]
	for i in arr[1:]:
		node = Node(i)
		if stk[-1].val > i:
			stk[-1].left = node
		else:
			while(len(stk) > 0 and stk[-1].val < i):
				prev = stk.pop()
			prev.right = node
		stk.append(node)
	return root

def display(subroot, indent = 1):
	if(subroot):
		display(subroot.left, indent + 1)
		print '->'.join(['' for i in range(indent)]), subroot.val
		display(subroot.right, indent + 1)

root = reconstruct_bst([3, 2, 0, 2.5, 5, 4, 6])
display(root)
	

