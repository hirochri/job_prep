'''
Insertion Sort

Best-case: O(n)
Worst-case: O(n^2)
Average-case: O(n^2)
Space: O(1)
Stable: Yes
'''

#Iterates over input list and for each element, figure
#out where to insert it in sorted list
def insertionsort(a):

  for i in range(1, len(a)):
    val = a[i]
    j = i

    while j > 0 and val < a[j-1]:
      #Look back and see if we can move into the spot of previous
      #If yes, we do, else we exit the loop and overwrite current position
      a[j] = a[j-1] #Overwrite current element with the one before it
      j -= 1

    a[j] = val

  return a #Again, not really needed as in place sort
