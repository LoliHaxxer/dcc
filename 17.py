tests = [["dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext", ], ["dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext", ], ]
class dir():
	def __init__(s,name="",parent=None):
		s.p = parent
		s.name = name
		if parent is not None: parent.add(s)
		s.sd = []
		s.f = []
	def add(s,new):
		if "."in new.name: s.f.append(new)
		else: s.sd.append(new)
	def all_files(s):
		r = []
		r.extend(s.f)
		for sd in s.sd: r.extend(sd.all_files())
		return r
	def get_absolute_path(s):
		if s.p is None: return s.name
		return s.p.get_absolute_path()+"/"+s.name
	def get_longest_absolute_path_file_absolute_path_length(s):
		longest = 0
		for f in s.all_files():
			l = len(f.get_absolute_path())
			if l > longest: longest = l
		return longest
	def read(string):
		r = dir()
		s = string.split("\n")
		lastlvl, at = 0, r
		for ss in s:
			lvl = ss.count("\t")
			sss = ss.replace("\t","")
			if lvl==0: r.name = sss
			else:
				if lvl <= lastlvl:
					for i in range(lastlvl-lvl+1): at = at.p
				at = dir(name=sss,parent=at)
			lastlvl = lvl
		return r
	def __str__(s): return s.name
for test in tests: print(test[0]," :\n",dir.read(test[0]).get_longest_absolute_path_file_absolute_path_length())
input()