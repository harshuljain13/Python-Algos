arr2 = list()

def max_heapify( j, length_arr2):
    left = 2*j+1
    right = 2*j+2
    if left< length_arr2:
        if arr2[left]>arr2[j]:
            largest = left
        else:
            largest = j
    else:
        largest = j
    if right <length_arr2:
        if arr2[right]>arr2[largest]:
            largest = right

    if largest != j:
        temp = arr2[largest]
        arr2[largest] = arr2[j]
        arr2[j] = temp
        max_heapify(largest,length_arr2)
        

def main():
    arr1 = map(int,raw_input().split())
    length_arr1 = len(arr1)

    for e in arr1:
        arr2.append(e)

    length_arr2 = len(arr2)
    j = length_arr2/2 - 1
    while j>=0:
        max_heapify(j,length_arr2)
        j = j-1
    print 'output heap:',arr2
        

if __name__ == '__main__':
    main()
