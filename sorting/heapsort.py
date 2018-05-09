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

