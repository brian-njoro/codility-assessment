def bubble_sort(arr):
    # work with a range 
    n = len(arr)
    for i in range(n):
        print("Outer loop")
        print(i)
        # i // or outer loop , represents the left pointer of our pair : iteration of each element in the collection 
        # inner loop will be used to move a comparison index : 
        # ? inner loop should iterate through the array up to the unsorted portion 
        for j in range(0, n-i-1):
         print("inner loop") 
         print(j)
        #  check if the currentl element is greater than the next element 
        # to sort in ascending > 
        # to sort in descending <
         if arr[j] < arr[j+1]:
            # swap the indexes  // according to your sort aspect 
            arr[j], arr[j+1] = arr[j+1] , arr[j]


arr = [64,34,25,12,22,11,90]
bubble_sort(arr)
print("Sorted array : " , arr)