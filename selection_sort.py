def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        mini = i
        for j in range (i+1,n):
            if (arr[mini] > arr [j] ) :
                mini = j
        arr[mini],arr[i] = arr[i],arr[mini]

arr=[1,3,5,2,4]
selection_sort(arr)
print(arr)
        
                