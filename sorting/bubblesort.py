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

    for j in range(len(a) - i - 1): #End becomes increasingly sorted so we can stop early
      if a[j] > a[j+1]:
        a[j], a[j+1] = a[j+1], a[j]
        swap = True

    if not swap:
      break

  return a #Modifies in place, so not really necessary

