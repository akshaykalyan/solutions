class stack:
	class Node(object):
		"""docstring for Node"""
		def __init__(self, data ,next):
			self.data = data
			self.next = next
	def __init__(self):
		self.head=None
	def push(self,data):
		self.head=(self.Node(data,self.head))
	def pop(self):
		old =self.head.data
		self.head=self.head.next
		return old
aww=stack()
aww.push(12)
aww.push(123)
print(aww.pop(),aww.pop())