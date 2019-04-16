class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def serialize(node):
	if node is None: return ""
	return node.val + " " + serialize(node.left) + " " + serialize(node.right)

def deserialize(string):
	def none(s): return None
	def deserialize(list):
		return Node(list.pop(0),none(list.pop(0))if list[0]==""else deserialize(list),none(list.pop(0))if list[0]==""else deserialize(list))
	return deserialize(string.split(" "))
	
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
