class BinTreeNode(object):
	def __init__(s,data,zero=None,one=None):
		s.data = data
		s.zero = zero
		s.one = one
	def count_unival(s):
		r = 1 if s.unival() else 0
		for i in s:
			if i.unival(): r+=1
		return r
	def unival(s):
		my = s.data
		for i in s:
			if my!=i.data:
				return False
		return True
	def leaf(s):
		return s.zero is None and s.one is None
	def __list__(s):
		r = []
		for node in (s.zero,s.one,):
			if node is not None: r=r.__add__([node,]).__add__(node.__list__())
		return r
	def __iter__(s):
		return s.__list__().__iter__()

tests = [
	BinTreeNode(0,BinTreeNode(1),BinTreeNode(0,BinTreeNode(1,BinTreeNode(1),BinTreeNode(1)),BinTreeNode(0))),
]
for test in tests:
	print(test.count_unival())
input()