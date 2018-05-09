'''
Quicksort

Best-case: O(nlogn)
Worst-case: O(n^2)
Average-case: O(nlogn)
Space: O(logn) best, O(n) avg
Stable: Usually not (some implementations exist)

Space complexity comes from recursion:
O(logn) calls on average, but worst case O(n)

Although merge sort has just the same complexity,
quick sort has a good constant factor hiddin by big-O notation
It outperforms merge sort and significantly outperforms selection/insertion sort
'''

#Divide and conquer style algorithm which first
#divides the full list into two smaller lists with
#low and high elements, then recursively sorts those

#Compared to merge sort (both divide and conquer)
#Mergesort: divide step does hardly anything and
#real work happens in combine step
#Quicksort: divide step does all real work, 
#combine step does nothing really

#Steps:
# 1. Pick a pivot (first, last, random, median, etc)
# 2. Partitioning: Reorder list so that all elements
#    less than pivot come before it, and all elements
#    greater than pivot come after (equal go either way)
#    After partitioning, pivot is in its final position
# 3. Recursively apply above steps so list of smaller
#    elements and list of bigger elements


def quicksort(a, l, h): #Called with 0, len(a)-1
  if l < h:
    p = partition(a, l, h)
    quicksort(a, l, p-1) #Before partition
    quicksort(a, p+1, h) #After partition


#Takes last element as pivot, then puts pivot
#element in correct position with smaller elements
#to the left and greater elements to the right
def partition(a, l, h): #[l, h]
  p = a[h] #Last element is pivot
  i = l

  for j in range(l, h): #while j <= h-1, aka everything in front of pivot

    if a[j] <= p: #Current element to low zone if it is <= pivot
      a[i], a[j] = a[j], a[i] #Swap with start of high zone (i is where new end of low zone will be)
      i += 1 #Next low zone end
  
  a[i], a[h] = a[h], a[i] #Swap pivot into place

  return i #Pivots new home

