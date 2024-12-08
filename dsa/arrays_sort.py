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
   
	print(f"Bubble sorted: {arr}")  

    
#selection sort
def my_selection_sort(arr):
    n = len(arr)
    print(f"Array before sorting: {arr}")
    for i in range(n-1):
        min_index = i
        
        
        print(f"Current min_index: {min_index} = {i}")
        for j in range(i+1, n):
            print(f"is {arr[j]} less than {arr[min_index]}")
            if arr[j] < arr[min_index]:
                print(f"Yes {arr[j]} is less than {arr[min_index]}")
                #arr[i], arr[min_index] = arr[min_index], arr[i]
                #print(f"Array after swapping: {arr}")
                print(f"The swap value is {arr[j]} and {arr[min_index]} in position {j} and {i}")
                min_index = j
                print(f"The value of min_index after updating: {min_index} = {arr[min_index]}")
            else:
                print(f"No {arr[j]} is not less than {arr[min_index]}")
         
        
        print(f"Before swapping: {arr[i]} - {arr[min_index]}")       
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"After swapping: {arr[i]} - {arr[min_index]}")      
        print(f"{i} - {arr[i]}")
    
        
    print(f"Selection sorted: {arr}")














def selection_sort(arr):
    n = len(arr)
    
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        min_value = arr.pop(min_index)
        arr.insert(i, min_value)
        
    print(f"Selection sorted: {arr}")     

def v2_selection_sort(arr):
    n = len(arr)  # Get the length of the array

    for i in range(n - 1):  # Iterate through the array (n-1 passes)
        min_index = i  # Assume the current element is the smallest

        # Find the smallest element in the unsorted portion
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # Update min_index if a smaller element is found

        # Swap the smallest element with the element at position i
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap using tuple unpacking

    print(f"Sorted array: {arr}")  # Print the sorted array
