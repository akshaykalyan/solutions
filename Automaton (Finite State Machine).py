class Automaton(object):
	class Node(object):
		def __init__(self, data,zero,one):
				self.data = data
				self.zero = zero
				self.one = one
	def __init__(self):
		self.q1=self.Node(False,None,None)
		self.q2=self.Node(True,None,None)
		self.q3=self.Node(False,None,None)
		self.q1.zero=self.q1
		self.q1.one=self.q2
		self.q2.one=self.q2
		self.q2.zero=self.q3
		self.q3.zero=self.q2
		self.q3.one=self.q2
	def read_commands(self, commands):
		t=self.q1
		for x in commands:
			if x=="1":
				t=t.one
			if x=="0":
				t=t.zero
		return t.data
my_automaton = Automaton()
print(my_automaton.read_commands(["1", "0", "0", "1"]))