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

#root1 = reconstruct_bst([3,1,  7])
#root2 = reconstruct_bst([5,3.5, 6])
root1 = reconstruct_bst([3, 2, 0, 2.5, 5, 4, 6])
display(root1)
print '===================='
root2 = reconstruct_bst([3.5, 1, 0.5, 1.5, 7, 6, 8])
display(root2)
print '===================='

def double_order(root1, root2):
	stk1 = []
	stk2 = []
	cur1 = root1
	cur2 = root2
	while True:
		while(cur1 != None):
			stk1.append(cur1)
			cur1 = cur1.left
		while(cur2 != None):
			stk2.append(cur2)
			cur2 = cur2.left
		if(len(stk1) == 0 and len(stk2) == 0):
			break
		# It's possible that cur1 or cur2 be set as None, 
		# That's OK, because the stak is not empty, the loop continues
		if(len(stk1) > 0 and (len(stk2) == 0 or  stk1[-1].val < stk2[-1].val)):
			cur1 = stk1[-1]
			print stk1.pop().val
			cur1 = cur1.right
		else:
			cur2 = stk2[-1]
			print stk2.pop().val
			cur2 = cur2.right

double_order(root1, root2)
