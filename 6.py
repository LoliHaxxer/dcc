memory_at = 1
memory = {}
dereferrer = {}
def new(class_name,*a,**b):
	global memory_at
	new = class_name(*a,**b)
	memory[memory_at] = new
	dereferrer[new] = memory_at
	memory_at+=1
	return new
def ref(pointer):
	if pointer==0: return None
	try:
		return memory[pointer]
	except:
		print(memory)
		print(dereferrer)
		raise
def deref(obj):
	try:
		return dereferrer[obj]
	except:
		print(memory)
		print(dereferrer)
		raise

class xor_list():
	class node:
		def __init__(self,data=None):
			self.data = data
			self.link = 0
		def enlink(self,pointer):
			self.link ^= pointer
		def other(self,pointer):
			return self.link ^ pointer
	def __init__(self):
		self.head = new(xor_list.node)
	def add(self, data):
		nn = new(xor_list.node, data)
		last = self.get_last()
		last.enlink(deref(nn))
		nn.enlink(deref(last))
	def get(self, i):
		atp = deref(self.head)
		last = 0
		try:
			while i>=0:
				next = ref(atp).other(last)
				last = atp
				atp = next
				i -= 1
			return ref(atp).data
		except AttributeError:
			raise IndexError("xor_list index out of range")
	def get_last(self):
		at = self.head
		last = 0
		while 1:
			next = at.other(last)
			if next==0: break
			last = deref(at)
			at = ref(next)
		return at
	def __len__(self):
		atp = deref(self.head)
		last = 0
		r = 0
		while 1:
			next = ref(atp).other(last)
			if next==0:break
			last = atp
			atp = next
			r += 1
		return r
	def __iter__(self):
		class i:
			lastp = 0
			at = self.head
			def __next__(s):
				next = ref(s.at.other(s.lastp))
				if next is None: raise StopIteration
				s.lastp = deref(s.at)
				s.at = next
				return s.at
		return i()
	def tolist(self):
		r = []
		for node in self:
			r.append(node.data)
		return r
	def __str__(self):
		return tolist(self).__str__()

xorlist = new(xor_list)
xorlist.add("index starts at zero")
xorlist.add("index starts at one")
print(xorlist.get(0))
print(xorlist.get(1))
print(xorlist.tolist())
input()
