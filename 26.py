class node(object):
	def __init__(s,v=None,n=None):
		s.v=v
		s.n=n
class singly_linked_list(object):
	def __init__(s):
		s.h=node()
	def last(s):
		at = s.h
		while at.n is not None: at=at.n
		return at
	def add(s,addend):
		s.last().n = addend
	def extend(s,iterable):
		at = s.last()
		for i in iterable:
			at.n = at = node(v=i)
	def rem_last(s,k):
		if k<=0: return
		rem=at=s.h.n
		for i in range(k):
			at=at.n
		while at.n is not None:
			at=at.n
			rem=rem.n
		rem.n=rem.n.n
input("hi")