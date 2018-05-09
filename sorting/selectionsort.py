'''
Selection Sort

Best-case: O(n^2)
Worst-case: O(n^2)
Average-case: O(n^2)
Space: O(1)
Stable: With swapping no
        If inserting min element at spot and shifting
        rest of list over, yes -> but leads to O(n^2) writes
'''

#Goes through list, finds lowest item and swaps it to
#the front (stays in place if it is the lowest). 
#Moves up one, and repeats the process until the last element is reached
def selectionsort(a):
  for i in range(len(a)):
    min_idx = i
    for j in range(i+1, len(a)):
      if a[j] < a[min_idx]:
        min_idx = j

    if min_idx != i:
      a[i], a[min_idx] = a[min_idx], a[i]

  return a #Does it in place, not technically needed
