# def fun(n):
#     if n > 0:
#         # print(n)
#         x = fun(n-1)
#         print(x)
#         fun(n-1)
# fun(3)
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
def maxDepth(node):
	if node is None:
		return 0
	else:
		lDepth = maxDepth(node.left)
		rDepth = maxDepth(node.right)
		if (lDepth > rDepth):
			print(lDepth,rDepth)
			return lDepth+1
		else:
			print(lDepth,rDepth)
			return rDepth+1
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Height of tree is %d" % (maxDepth(root)))

