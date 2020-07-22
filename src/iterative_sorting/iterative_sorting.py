# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    n = len(arr)                                # we'll be using this a lot, so just give it its own var
    for i in range(0, n - 1):
        # cur_index = i
        # smallest_index = cur_index
        min = i                                 # simplified var
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # for j in range(i + 1, n):
        #     if arr[j] < arr[smallest_index]:
        #         smallest_index = j
        for j in range(i+1, n):                 # for the one to the right of i (for the duration of the array):
            if arr[j] < arr[min]:               # if that one is smaller than the i in question:
                min = j                         # it then becomes the smallest in the comparison set

        # TO-DO: swap                           # so switch their positions
        # arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        arr[i], arr[min] = arr[min], arr[i]   

    return arr                                  # after the whole array's been looped through, return it


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    n = len(arr)                                # we'll be using this a lot, so just give it its own var
    for i in range(n):                          # for every i in the array (no edits):
        for j in range(n - 1):                  # for every item except the last one (because it will be switched ??)
            if arr[j] > arr[j+1]:                   # if that one is smaller than the i to the right:
                arr[j], arr[j+1] = arr[j+1], arr[j] # switch their positions

    return arr                                  # after the whole array's been looped through, return it

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
