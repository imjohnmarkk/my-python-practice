#bubble sort
def bubble_sort(arr):
    
	n = len(arr)
    
	for i in range(n-1):
		swapped = False
		for j in range(n-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True
                
		if not swapped:
			break
   
	print(f"Sorted array: {arr}")  
    
#selection sort
def selection_sort(arr):
    n = len(arr)
    
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        min_value = arr.pop(min_index)
        arr.insert(i, min_value)
        
    print(f"Sorted array: {arr}")     
    