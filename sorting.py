import random

def main():

  for i in range(1000):
    test = random.sample(range(100), 100)
    correct = sorted(test)

    #assert(td_mergesort(test) == correct)
    #assert(bubblesort(test) == correct)
    #assert(selectionsort(test) == correct)
    #assert(insertionsort(test) == correct)

    #quicksort(test, 0, len(test)-1)
    #assert(test == correct)

    #countingsort(test, 99)
    #assert(test == correct)

    #assert(heapsort(test) == correct)


#Stable: The original order of elements with 
#        equal key values is preserved

#List used interchangeably with array throughout

#==================================================================================
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


#==================================================================================
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



#==================================================================================
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


#==================================================================================
'''
Bubble Sort

Best-case: O(n)
Worst-case: O(n^2)
Average-case: O(n^2)
Space: O(1)
Stable: Yes
'''

#Repeatedly passes over list, swapping elements if
#they are in the wrong order. Keep passing through
#the list until no more swaps are needed. Larger elements
#bubble up to the end of the list
#The nonoptimized version is simply two loops: 
# for i in range(len(a))
#    for j in range(len(a) - i - 1)
#Since the last i elements are already sorted, it gets
#cut down over time, but this version runs in O(n^2)
#even if the array is already sorted
def bubblesort(a):
  for i in range(len(a)):
    swap = False

    for j in range(len(a) - i - 1):
      if a[j] > a[j+1]:
        a[j], a[j+1] = a[j+1], a[j]
        swap = True

    if not swap:
      break

  return a #Modifies in place, so not really necessary

#Crappy version from memory
#Exits early when stuff is already sorted
#But goes up to the last element in the array
#every time even though the end is increasingly sorted
#with each iteration. Above version is better
def bubblesort_hiro(a): 
  flip = True

  while flip:
    flip = False

    for i in range(len(a)-1):
      if a[i] > a[i+1]:
        a[i], a[i+1] = a[i+1], a[i]
        flip = True

  return a

#==================================================================================
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

#==================================================================================
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

#==================================================================================

'''
Binary heap

        Average  Worst
Space:  O(n)     O(n)
Search: O(n)     O(n)
Insert: O(1)     O(logn)
Delete: O(logn)  O(logn)
Peek:   O(1)     O(1)
* A complete binary tree which satisfies the heap ordering property
  1. min-heap property: value of each node is >= value of its parent
     root is the minimum value
  2. max-heap property: value of each node is <= value of its parent
     root is the maximum value

  Highest/lowest priority element is always stored at root.
  A heap is *not* a sorted structure and can be regarded as partially ordered

* To guarantee logarithmic performance, tree needs to 
  stay balanced, so can use a complete binary tree where
  each level but the last has all its nodes and the last level
  is filled from left to right. Thus hight always O(logn) for n nodes

* Since its a complete binary tree, we can use an array to store its level order traversal
  The root is the second item in the array (index 1) for mathematical convenience
  For the k-th element of the array
    * Left child is located at 2*k
    * Right child is located at 2*k + 1
    * Parent is located at k/2

* Because its a complete binary tree, the left child of
  a parent node at position p is 2p. The right child is 2p + 1.
  To find the parent of a node at position n simply go to n/2

* Insertion: New element is initially appended to
  the end of the array as the last element. The heap
  property is repaired by comparing the new element
  with itsparent and moving it up a level (swap w/
  parent) if needed aka percolating up. Repeat until
  new element is in a good spot in relation to its parent

* Deletion of Min: Minimum/maximum element can always be 
  found at the root. We remove the root and replace
  it with the last element of the heap, then restore
  the heap property by percolating down. To swap down,
  we swap the node with the smallest child that is less
  than that node, until we get to a spot where the node
  is smaller than both of its children

* Building heap: The naive method is to simply go through
  the input list and insert each element into the heap
  one at a time. These n insertions have logn cost each
  so this method is O(nlogn).

  However starting with an entire list, we can build the
  heap in O(n) operations, although its a little tricky.

  We start out in the middle of the tree (halfway through the list)
  and work our way towards the root (Percolate root of each subtree 
  down as needed). Since the binary tree is complete, 
  any nodes past the halfway point are leaves and will have no children.
  Ex: 7 nodes -> nodes 1-3 have children, 4-7 don't
  Ex: 5 nodes (lower right empty) -> nodes 1-2 have children, 3-5 don't
  The percolate_down method ensures that the biggest elements work themselves 
  all the way to the bottom.
  If all subtrees at some height (where bottom level has height 0)
  have been heapified, the trees at height +1 can be heapified by
  sending their root down along the path of min-valued children.
  Because this takes O(height) operations per node and the height
  is floor(logn), some math happens and the cost of heapifying
  all subtress is O(n)
'''

#Min heap
class BinaryHeap:
  def __init__(self):
    self.heaplist = [0]
    self.heapsize = 0

  def percolate_up(self, i):
    while i // 2 > 0: #While parent exists
      if self.heaplist[i] < self.heaplist[i // 2]:
        self.heaplist[i], self.heaplist[i // 2] = self.heaplist[i // 2], self.heaplist[i]
      i //= 2 #Set current index to that of our parent which we just took place of

  def insert(self, e):
    self.heaplist.append(e)
    self.heapsize += 1
    self.percolate_up(self.heapsize)

  def percolate_down(self, i):
    while i * 2 <= self.heapsize: #While children exist
      mc = self.min_child(i)
      if self.heaplist[i] > self.heaplist[mc]:
        self.heaplist[i], self.heaplist[mc] = self.heaplist[mc], self.heaplist[i]
      i = mc #Set current index to the min child we just took the place of
  
  def min_child(self, i):
    #Percolate down checks for left child existance but not right
    if i * 2 + 1 > self.heapsize:
      return i * 2
    else: #Right child exists
      return i * 2 + (self.heaplist[i*2+1] < self.heaplist[i*2])
      #Will +1 if right child is smaller, else picks left child

  def delete_min(self):
    deleted = self.heaplist[1]
    self.heaplist[1] = self.heaplist[self.heapsize] #1 indexed..
    self.heapsize -= 1
    self.heaplist.pop()
    self.percolate_down(1)
    return deleted
  
  def get_min(self):
    return self.heaplist[1]

  def build_heap(self, a):
    self.heapsize = len(a)
    self.heaplist = [0] + a[:]

    i = len(a) // 2
    while i:
      self.percolate_down(i)
      i -= 1

'''
Heapsort

Best-case: O(nlogn)
Worst-case: O(nlogn)
Average-case: O(nlogn)
Space: O(1)
Stable: No
'''

def heapsort(a):
  heap = BinaryHeap()
  heap.build_heap(a)

  ret = []
  while heap.heapsize:
    ret.append(heap.delete_min())

  return ret

if __name__ == '__main__':
  main()

