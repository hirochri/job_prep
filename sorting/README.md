Stable: The original order of elements with equal key values is preserved


Sort|Best|Worst|Average|Space|Stable|
|---|---|---|---|---|---|
|Bubble|O(n)|O(n^2)|O(n^2)|O(1)|Yes|
|Insertion|O(n)|O(n^2)|O(n^2)|O(1)|Yes|
|Selection|O(n^2)|O(n^2)|O(n^2)|O(1)|\*No|
|Counting|O(k+n)|O(k+n)|O(k+n)|O(k+n)|Yes|
|Merge|O(nlogn)|O(nlogn)|O(nlogn)|O(n)|Yes|
|Quick|O(nlogn)|O(n^2)|O(nlogn)|O(logn) best, O(n) avg|Usually not|
|Heap|O(nlogn)|O(nlogn)|O(nlogn)|O(1)|No|

\* With swapping, not stable. If inserting min element at spot and shifting rest of list over, yes (But that requires O(n^2) writes)
For counting sort, n = number of elements in input list. k = range of input
