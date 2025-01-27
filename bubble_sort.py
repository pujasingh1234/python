def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize if the list is already sorted
        swapped = False
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no two elements were swapped, then the list is sorted
        if not swapped:
            break

# Input list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Sort the list using bubble sort
bubble_sort(numbers)

# Output the sorted list
print("Sorted list:", numbers)
