'''
Merge Sort

Best-case: O(nlogn)
Worst-case: O(nlogn)
Average-case: O(nlogn)
Space: O(n)
Stable: Yes


Recurrence relationship
T(n) = 2T(n/2) + n
       ^       ^- merge step where we sort/combine left and right halves
       Calling mergesort on left and right halves

Apply algorithm to two lists of half the size of original list
and add the n steps taken to merge two resulting lists

O(nlogn) can be thought about as tree:

      N      1*(N) = N
    /  \
  N/2  N/2   2*(N/2) = N
 /  \ /  \
N/4.....N/4  4*(N/4) = N

N work to be done at each layer, logn layers so nlogn


Merge sort can be useful for sorting linked lists in O(nlogn) time

'''

#Top-down
#Recursively split lists into sublists until they are size 0 or 1
#Merge those sublists to produce sorted lists and return up the call stack
def td_mergesort(a):
  #When starting with a full list, [x] basecase will always be hit, 
  #but we want to account for empty initial input too
  if len(a) < 2: 
    return a

  m = len(a) // 2
  l = td_mergesort(a[:m])
  r = td_mergesort(a[m:])

  return merge(l, r)

def merge(x, y):
  ret = []

  while x and y:
    if x[0] <= y[0]: #Maintain stability
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

def alt_merge(xs, ys):
  i = j = 0
  ret = []

  while i < len(xs) and j < len(ys):
    x,y = xs[i], ys[j]

    if x <= y: #Maintain stability
      ret.append(x)
      i += 1
    else:
      ret.append(y)
      j += 1

  if i == len(xs):
    ret += ys[j:]
  else:
    ret += xs[i:]

  return ret

#Bottom-up
#Merge pairs of adjacent lists of length 1, then of
#length 2, then of length 4 until whole list is merged
#Since all elements are touched in every iteration, 
#we want to 
def bu_mergesort(a):
  if not a:
    return []

  chunks = [[x] for x in a]

  while len(chunks) > 1: #Until we have one big list
    chunks = merge_chunks(chunks)

  return chunks[0]

def merge_chunks(chunks):
  ret = []

  #Merge adjacent chunks
  for i in range(0, len(chunks)-1, 2):
    ret.append(merge(chunks[i], chunks[i+1]))
  #*Alt way to do this


  #Add odd last list to be sorted next cycle
  if len(chunks) % 2 == 1:
    ret.append(chunks[-1])

  return ret

'''
Alt

for i, j in zip(range(0, len(chunks)-1, 2), range(1, len(chunks), 2)):
  ret.append(merge(chunks[i], chunks[j]))

for i in range(len(chunks) // 2):
  ret.append(merge(chunks[i*2], chunks[i*2 + 1]))
  #i=0 -> 0, 1 #i=1 -> 2, 3 #i=2 -> 4, 5
'''

