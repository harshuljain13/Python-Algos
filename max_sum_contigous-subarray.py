def maxSubArray(a):
        max_so_far =a[0]
        curr_max = a[0]
     
        for i in range(1,len(a)):
            curr_max = max(a[i], curr_max + a[i])
            max_so_far = max(max_so_far,curr_max)
         
        print max_so_far

if __name__=='__main__':
    maxSubArray([45,-25,2,34,55])
