def main():
  #TODO write tests for these
  pass

def binarySearch(self, nums, target):
  l, r = 0, len(nums) - 1
  
  #leq because it might be a list with one value 
  #and we still need to check equality, only need
  #to return when l > r
  while l <= r:
    m = l + (r-l) // 2
    
    if nums[m] > target:
      r = m - 1 #Reduce right side of search space
    elif nums[m] < target:
      l = m + 1 #Reduce left side of search space
    else:
      return True
      
  return False

#Return the index if the target is found,
#otherwise return the index where it would be if it were
#inserted in order. (Like bisect.bisect_left)

def binarysearch_insert(nums, target):
  l, r = 0, len(nums) #Want to be able to insert past last element of array
  #Usually len(nums)-1 for search only
      
  while l < r:
    m = l + (r-l) // 2
    
    if nums[m] >= target:
      #Reduce right side of search space
      #Trying to find first element that is larger or equal to target
      #Want to include this element and keep moving right boundary
      #to the left if mid is another element that is greater or equal
      r = m
    else:
      #Reduce left side of search space
      l = m + 1
          
  return l


if __name__ == "__main__":
  main()
