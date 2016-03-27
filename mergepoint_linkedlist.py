class LL(object):
    def __init__(self):
        self.data=None
        self.link=None

    def update(self,data):
        self.data=data
    def getdata(self):
        return self.data

def create_list(data):
    start = LL()
    start.update(data[0])
    prev=start
    for i in range(1,len(data)):
        curr = LL()
        curr.update(data[i])
        prev.link=curr
        prev=curr
    return start

def callength(x):
    length=0
    while x:
        length+=1
        x=x.link
    return length

def findmerge(s1,s2):
    m=callength(s1)
    n=callength(s2)
    d=n-m
    if m>n:
        temp=s1
        s1=s2
        s2=temp
        d=m-n
    for i in range(d):
        s2=s2.link
    while s1 and s2:
        if s1.getdata()==s2.getdata():
            return s1.getdata()
        s1=s1.link
        s2=s2.link
    return None
    
data1=raw_input().split(' ')
data2=raw_input().split(' ')

s1=create_list(data1)
s2=create_list(data2)
print findmerge(s1,s2)
