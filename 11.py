tests = [["de",["dog","deer","deal",]],]
def nodifyList(list):
	if len(list)>0:
		root = newNode(list[0])
		for i in range(1,len(list)):
			insert(root, list[i])
		return root
	else: return None
class newNode:
	def __init__(self, data):  
		self.key = data 
		self.count = 1
		self.left = None
		self.right = None
	def __str__(s):
		return str(s.key)+" "+str(s.count)+" "+str(s.left,)+" "+str(s.right,)
def inorder(root): 
	if root is not None: 
		inorder(root.left) 
		print(root.key,"(", root.count,")",  
								 end = " ")  
		inorder(root.right)
def insert(node, key):
	if node is None: 
		k = newNode(key) 
		return k
	if key == node.key: 
		(node.count) += 1
		return node 
	if key < node.key:  
		node.left = insert(node.left, key)  
	else: 
		node.right = insert(node.right, key)
	return node
def minValueNode(node): 
	current = node
	while current.left is not None:  
		current = current.left  
	return current
def deleteNode(root, key):
	if root is None: 
		return root
	if key < root.key: 
		root.left = deleteNode(root.left, key)
	elif key > root.key:  
		root.right = deleteNode(root.right, key)
	else:
		if root.count > 1: 
			root.count -= 1
			return root
		if root.left == None: 
			temp = root.right 
			return temp 
		elif root.right == None: 
			temp = root.left 
			return temp 
		temp = minValueNode(root.right)
		root.key = temp.key
		root.right = deleteNode(root.right, temp.key) 
	return root
def autoComplete(root, key):
	r = set()
	if root is None:
		return r
	if key in root.key:
		r.add(root.key)
	r.update(autoComplete(root.left,key))
	r.update(autoComplete(root.right,key))
	return r
	
for test in tests:
	troot = nodifyList(test[1],)
	print(test," :\n"+str(autoComplete(troot,test[0])))
input()