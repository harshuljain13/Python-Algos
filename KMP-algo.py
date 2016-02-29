def failure_function(p):
   l=len(p)
   f=[0]*l
   j=0 
   for i in range(1,l):
      while j>=0 and p[j]!=p[i]:
         if j-1>=0: j=f[j-1]
         else: j=-1 
      j+=1
      f[i]=j
   return f

def find_occurrences(t,p):
   f=failure_function(p)
   lt,lp=len(t),len(p)
   j=0
   for i in range(lt):
      while j>=0 and t[i]!=p[j]:
         if j-1>=0: j=f[j-1]
         else: j=-1
      j+=1  
      if j==lp:
         j=f[lp-1]
         print i-lp+1

find_occurrences('abcdabcdabcd','ab')
