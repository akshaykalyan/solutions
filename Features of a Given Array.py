from collections import OrderedDict
class Array(object):
    def __init__(self, arr = []):
        self.arr = arr
    
    def num_elements(self):
        return len(self.arr)
    def num_values(self):
        return len(set(self.arr))
    
    def start_end(self):
        return [self.arr[0],self.arr[-1]]
        
    def range_(self):
        return [min(self.arr),max(self.arr)]
        
    def largest_increas_subseq(self):
        t=[]
        main=[]
        for x in self.arr:
            if t==[] or t[-1]<x:
                t.append(x)
            else:
                main.append(t)
                t=[x]
        main.append(t)
        t=[len(x) for x in main ]
        t=t.index(max(t))
        return main[t] if len(main[t])>2 else "No increasing subsequence"
        
    def largest_decreas_subseq(self):
        t=[]
        main=[]
        for x in self.arr:
            if t==[] or t[-1]>x:
                t.append(x)
            else:
                main.append(t)
                t=[x]
        main.append(t)
        t=[len(x) for x in main ]
        t=t.index(max(t))
        return main[t] if len(main[t])>2 else "No decreasing subsequence"
        
    def __str__(self):
        d = OrderedDict([('1.number of elements', self.num_elements()), 
('2.number of different values', self.num_values()), 
('3.first and last terms', self.start_end()),
('4.range of values', self.range_()), 
('5.increas subseq', self.largest_increas_subseq()), 
('6.decreas subseq', self.largest_decreas_subseq())])
        return str(d)
arr = [345, 32, 45, 12, 45, 47, 49, 55, 90, 104, 20, 30, 34]
c = Array(arr)
print (c.__str__())
