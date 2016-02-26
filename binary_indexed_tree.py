BIT = list()
array= list()

## enter the numbers in "1 2 3 4 5 6"(space) format
def update(x,val):
    while x <= len(array):
        BIT[x] += val
        x += x&-x

def query(x):
    sum_value=0
    while x>0:
        sum_value += BIT[x]
        x -= x&-x
    print 'sum:', sum_value    
    
def main():
    print 'enter the values for the array'
    global array
    array = map(int,raw_input().split())

    for i in range(len(array)+1):
        BIT.append(0)
        
    for i in xrange(1,len(array)):
        update(i,array[i-1])

    print 'enter the number upto which sum of numbers need to be found'
    x = int(raw_input())
    query(x)
    
if __name__ == '__main__':
    main()
