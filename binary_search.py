def main():
  #TODO write tests for these
  pass

def binarySearch(self, nums, target):
  l, r = 0, len(nums) - 1
  
  #leq because it might be a list with one value 
  #and we still need to check equality, only need
  #to return when l > r
  while l <= r:    #*
    m = l + (r-l) // 2
    
    if nums[m] > target:
      r = m - 1 #Reduce right side of search space
    elif nums[m] < target:
      l = m + 1 #Reduce left side of search space
    else:
      return True
      
  return False

#* If you have a problem where you are guaranteed an answer (can be value or just index to put value), you can do l < r and return nums[l]
#  If you aren't guaranteed an answer, you need to be able to check when l == r and then return false if you end
#  up moving l > r
#  Binary search and insert has l < r since it has a guaranteed insert point always

#Return the index if the target is found,
#otherwise return the index where it would be if it were
#inserted in order. (Like bisect.bisect_left)

def binarysearch_insert(nums, target):
  l, r = 0, len(nums) #Want to be able to insert past last element of array
  #Usually len(nums)-1 for search only -> don't care about adding new elements
      
  while l < r: #Guaranteed to always find an insertion point
    m = l + (r-l) // 2
    
    if nums[m] >= target: #$
      #Reduce right side of search space
      #Trying to find first element that is larger or equal to target
      #Want to include this element and keep moving right boundary
      #to the left if mid is another element that is greater or equal
      r = m
    else:
      #Reduce left side of search space
      l = m + 1
          
  return l
  #Returns index at which target is or leftmost index where it should be inserted
  #To make this return the rightmost index at which target should be inserted,
  #we can make the $ conditional simply nums[m] > target. This then makes it
  #so in the end l is the index one past our rightmost target. To know if
  #the rightmost target itself exists, simply check nums[l-1] == target


if __name__ == "__main__":
  main()
