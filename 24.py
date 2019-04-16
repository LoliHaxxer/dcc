class node:
	def __init__(s,p,v=None,z=None,o=None):
		s.p = p
		s.v = v
		s.z = z
		s.o = o
		s.locked = 0
	def is_locked(s):
		return s.locked
	def lock(s):
		for c in s.gds()+s.gps():
			if c.locked: return 0
		s.locked = 1
		return 1
	def unlock(s):
		for c in s.gds()+s.gps():
			if c.locked: return 0
		s.locked = 0
		return 1
	def gps(s):
		if s.p is None: return []
		r = []
		r.append(s.p)
		r.extend(s.p.gps())
		return r
	def gds(s):
		r = []
		for d in (s.z,s.o,):
			if d is not None:
				r.append(d)
				r.extend(d.gds())
		return r
input("lol did u rly think anything would happen here?")