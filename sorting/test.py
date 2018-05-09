import random
from mergesort import *

def main():

  for i in range(1000):
    test = random.sample(range(100), 100)
    correct = sorted(test)

    assert(test_td_mergesort(test) == correct)
    #assert(bu_mergesort(test) == correct)
    #assert(bubblesort(test) == correct)
    #assert(selectionsort(test) == correct)
    #assert(insertionsort(test) == correct)

    #quicksort(test, 0, len(test)-1)
    #assert(test == correct)

    #countingsort(test, 99)
    #assert(test == correct)

    #assert(heapsort(test) == correct)
  print("Sort passed")

main()
