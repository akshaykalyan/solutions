class circular_queue(object):
				
	class Node(object):
		def __init__(self, data,next):
			self.data = data
			self.next = next
	def __init__(self):
		self.tail = None
		self.size =0
	def enqueue(self,e):
		new= self.Node(e,self.Node)
		if self.size==0:
			new.next=new
		else:
			new.next=self.tail.next
			self. tail. next = new
		self.tail=new
		self.size+=1
	def dequeue(self):
		old=self.tail.next
		if self.size==1:
			self.tail=None
		else:
			self.tail.next=old.next
		self.size-=1
		return old.data
x=circular_queue()

for i in range (3):
	x.enqueue(i)
	# print(x.tail.data)
	# print(x.tail.next)
for i in range(3):
	print(x.dequeue())