class node(object):
	def __init__(s,v,next=None):
		s.v = v
		s.next = next
	def link(s,next):
		s.next = next
		return next
	def __eq__(s,o): return s.v == o.v
def gi(a,b,):
	sb = b
	while 1:
		if a is None: break
		b = sb
		while 1:
			if b is None: break
			if a==b: return a
			b = b.next
		a = a.next
	return None
def get_intersect(A,B,):
	while A!=B:
		A = B if A.next is None else A.next
		B = A if B.next is None else B.next
	return A
sll1 = node(3)
sll1.link(node(7)).link(node(8)).link(node(10))
sll2 = node(99)
sll2.link(node(1)).link(node(7)).link(node(8)).link(node(10))
print(gi(sll1,sll2).v,get_intersect(sll1,sll2).v,sep="\n")
input()