# a complete binary tree
# nodes are left as far as possible

def heapify(arr, n, i):
    largest = i
    l = 2*i+1
    r = 2*i+2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def insert(array, newNum):
    size = len(array)

    if size == 0:
        array.append(newNum)

    else:
        array.append(newNum)
        for i in range((size // 2) - 1, -1, -1):
            heapify(array, size, i)


def deleteNode(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break
    array[i], array[size-1] = array[size-1], array[i]
    array.remove(size-1)
    for i in range((len(array)//2)-1, -1, -1):
        heapify(array, len(array), i)


def heapsort(arr):
    n = len(arr)

    #Build a maxheap, since last parent will be ((n//2) - 1), we can start at that location
    for i in range(n //2 -1, -1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    


arr = []
insert(arr, 3)
insert(arr, 4)
insert(arr, 5)
insert(arr, 6)
insert(arr, 7)
insert(arr, 8)
insert(arr, 2)


arr = [35, 78, 458, -8, 0, 47]
heapsort(arr)

