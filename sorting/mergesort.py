'''
Merge Sort

Best-case: O(nlogn)
Worst-case: O(nlogn)
Average-case: O(nlogn)
Space: O(n)
Stable: Yes


Recurrence relationship: T(n) = 2T(n/2) + n
Apply algorithm to two lists of half the size of original list
and add the n steps taken to merge two resulting lists

O(nlogn) can be thought about as tree:

      N      1*(N) = N
    /  \
  N/2  N/2   2*(N/2) = N
 /  \ /  \
N/4.....N/4  4*(N/4) = N

N work to be done at each layer, logn layers so nlogn

'''

#Top-down
#Recursively split lists into sublists until they are size 0 or 1
#Merge those sublists to produce sorted lists and return up the call stack
def td_mergesort(a):
  if len(a) < 2:
    return a

  m = len(a) // 2
  l = td_mergesort(a[:m])
  r = td_mergesort(a[m:])

  return merge(l, r)

def merge(x, y):
  ret = []

  while x and y:
    if x[0] < y[0]:
      ret.append(x[0])
      x.remove(x[0]) #Removes the 1st occurence in list, so order is maintained
    else:
      ret.append(y[0])
      y.remove(y[0])

  if x:
    ret += x
  else:
    ret += y

  return ret

#Bottom-up
#Merge pairs of adjacent lists of length 1, then of
#length 2, then of length 4 until whole list is merged
#Since all elements are touched in every iteration, 
#we want to 


