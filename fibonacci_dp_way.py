def main():
    print 'enter the number for fibonacci series'
    n =int(raw_input())
    fib_array = list()
    print 'fibonacci series:'
    for i in range(n):
        if i<2:
            fib_array.append(1)
        else:
            fib_array.append(fib_array[i-1] + fib_array[i-2])
        print fib_array[i]
    
if __name__=='__main__':
    main()
