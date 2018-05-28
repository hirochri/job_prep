To Review

\* Building trees from different traversals

\* BST is a sorted range that has best case O(logn) search/insert/delete if tree is balanced (or O(n) if unbalanced, but most implementations would be a self balanced BST like AVl or Red-Black trees) vs. if you use an array for storing a sorted range you have O(logn) search with binary search, but O(n) deletion/insertion since you have to shift everything over
 
\* Any recursive Pre/In/Post-order traversal is a DFS as it uses built in call stack, otherwise you use a normal stack to do iterative DFS. BFS is your standard layer traversal using a queue
