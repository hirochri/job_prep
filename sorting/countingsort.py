'''
Counting sort

Best-case: O(k+n)
Worst-case: O(k+n)
Average-case: O(k+n)
Space: O(k+n)
Stable: Yes

n = # elements in input list
k = range of input

Space: O(k) for the map/list keeping track of count per key
       O(n) for the new sorted list (can also modify original list though)

Time: Two styles of loops, some over all n elements
      some over all k keys -> O(n+k)


Is efficient if the range of input data is not 
significantly larger than the number of objects to be sorted
'''

#Relies on keys being in a specific range
#Count how many occurences of each key there are
#and then write over input array using that information
def countingsort(a, k): #k is inclusive
  count = [0] * (k+1)

  for val in a:
    count[val] += 1

  idx = 0
  for i, c in enumerate(count):
    while c:
      a[idx] = i
      idx += 1
      c -= 1

  return a #Not necessary, modifies a in place
