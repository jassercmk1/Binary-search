def binary_search(arr, x):
    # Get the lower and upper bounds of the search range
    low = 0
    high = len(arr) - 1
    
    # Continue searching while there are still elements in the range
    while low <= high:
        # Find the middle index of the range
        mid = (low + high) // 2
        
        # Check if the middle element is the target
        if arr[mid] == x:
            return mid
        
        # If the middle element is less than the target, search the upper half
        elif arr[mid] < x:
            low = mid + 1
        
        # If the middle element is greater than the target, search the lower half
        else:
            high = mid - 1
    
    # If the target is not found, return -1
    return -1

# Get a list of integers from the user
my_list = [14, 37, 48, 4, 35, 21, 30, 7, 15, 42, 3, 38, 31, 20, 27, 19, 18, 24, 49, 10, 9, 44, 
           23, 33, 22, 47, 46, 26, 11, 16, 29, 50, 13, 25, 8, 43, 12, 2, 32, 39, 1, 36, 6, 28, 
           45, 5, 41, 17, 34, 40]

# Sort the list
my_list.sort()

# Get the target value from the user
target = int(input("Enter the target value: "))

# Call the binary_search() function to search for the target value in the list
result = binary_search(my_list, target)

# Check if the target was found and print the result
if result != -1:
    print("The target was found at index", result)
else:
    print("The target was not found in the list")
