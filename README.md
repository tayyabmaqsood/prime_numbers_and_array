This code is about rotate array and don't change prime number index.
We Rotate array by putting **last element of array at the start of the array** and shifting other elements of array by one index
like this
**Input:**
  arr = [4,6,8,10,12,8]
  print( rotate_array( arr, len(arr) - 1 )
**Output:**
  [8, 4, 6, 8, 10, 12]
  
But the tricky thing here is if some prime numbers are given in our array its index should not be changed in any case.
**Input:**
   [2,6,12,3,16,9,11,4,3,8,7,10]
 **Output:**
    [2, 10, 6, 3, 12, 16, 11, 9, 3, 4, 7, 8]
Here I am posting code.    
