def linear_search(arr, target):
    for i in range(len(arr)):       # for the entire arr:
        if arr[i] == target:        # if the target matches an existing item:
            return i                # return its location

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    first = 0                       # var for lowest
    last = len(arr)-1               # var for highest
    mid = 0                         # var for comparison item / starting point

    while first <= last:            # as long as the first is less than the last:
        mid = (first + last) // 2   # sets mid as the average center to eliminiate 50% of the data
        if arr[mid] < target:       # if the target is greater than the center, ignore the left
            first = mid+1           
        elif arr[mid] > target:     # if target is less than the center, ignore the right
            last = mid-1
        else:
            return mid              # or we found it right in the center, lucky guess!

    return -1  # not found