class doublyLL(object):
	class Node (object):
		def __init__(self, data,next,prev):
			self.data = data
			self.next = next
			self.prev = prev
	def __init__(self):
		self.header=self.Node(None,None,None)
		self.tailer=self.Node(None,None,None)
		self.size=0
		self.header.next=self.tailer
		self.tailer.prev=self.header
	def push(self,e):
		n=self.header.next
		self.header.next=self.Node(e,n,self.header)
		n.prev=self.header.next
	def pop(self):
		head=self.header.next
		self.header.next=head.next
		head.next.prev=self.header
		return head.data
x=doublyLL()
for c in range (10):
	x.push(c)
for c in range (10):
	print(x.pop())