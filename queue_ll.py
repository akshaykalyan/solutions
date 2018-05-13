class queue(object):
	"""docstring for queue"""
	class Node(object):
		def __init__(self,data,next):
			self.data = data
			self.next = next
	def __init__(self):
		self.head=None
		self.tail=None
		self.size=0
	def enqueue(self,e):
		new=self.Node(e,None)
		if self.size==0:
			self.head=new
		else:
			self.tail.next=new
		if self.size==1:
			print(id(self.head)==id(self.tail))
		self.tail=new
		self.size+=1
	def dequeue(self):

		answer=self.head.data
		self.head=self.head.next
		self.size-=1
		return answer
x=queue()
for i in range(5):
	x.enqueue(i) 

for i in range(5):
	print(x.dequeue()) 

