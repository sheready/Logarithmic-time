#This is an algorithm that reduces the size of the input data in each size.The number of operations reduces as the input size increases
#I will implement the binary search 
#To perform a binary search in an array we repeatedly divide the search interval in half.
#We begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty
#https://www.geeksforgeeks.org/complexity-analysis-of-binary-search/
#recursive binary search

import time 

def binarySearch(array, lowvalue, highvalue, searchValue):

  if lowvalue >= highvalue:
    mid = lowvalue + (highvalue -           lowvalue)//2
    #if element is at the middle
    if array[mid] == searchValue:
      return mid
    #If element is smaler than mid it is in the left subarray
    elif array[mid] > searchValue:
      return binarySearch(array, lowvalue, mid-1, searchValue)
    #else the element is in the right sub arra
    else:
      return binarySearch(array, mid+1,highvalue, searchValue)
  else:
    #element not in array
    return -1
start = time.time()
array = [45,29,61,21,40,31,82,90]
searchValue = 61

result = binarySearch(array, 0, len(array)-1, searchValue)
if result != -1:
  print("Element is at index %d" % result)
  print("Execution time is: {}".format(time.time() - start))
else:
  print("Element is not present in array")
  print("Execution time is: {}".format(time.time() - start))




