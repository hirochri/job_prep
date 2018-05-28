To Review

\* Building trees from different traversals

Post order has the root at the end, so once we find that we can split the inorder based on that root value
Since we know the right child root node from the postorder, we have to build the right subtree first before we get to the left subtree (opposite for preorder)

You have to ensure that preorder/postorder shrinks (can't just slice it) additionally between the left/right subtree call, as once we get to the second one we expect all the root nodes in the other to have been exhausted
```python
def helper(inorder, postorder):
  if not inorder:
    return None
            
  node = TreeNode(postorder.pop())
            
  idx = inorder.index(node.val)
            
  node.right = helper(inorder[idx+1:], postorder)
  node.left = helper(inorder[:idx], postorder)
            
  return node
```
```python
def helper(preorder, inorder):
  if not inorder:
    return None
    
  node = TreeNode(preorder[0])
  preorder.remove(node.val)
  #Import to remove ^ and then not just preorder[1:] since it doesn't have cumulative effect
            
  idx = inorder.index(node.val)
            
  node.left = helper(preorder, inorder[:idx])
  node.right = helper(preorder, inorder[idx+1:])
               
  return node
```

\* BST is a sorted range that has best case O(logn) search/insert/delete if tree is balanced (or O(n) if unbalanced, but most implementations would be a self balanced BST like AVl or Red-Black trees) vs. if you use an array for storing a sorted range you have O(logn) search with binary search, but O(n) deletion/insertion since you have to shift everything over
 
\* Any recursive Pre/In/Post-order traversal is a DFS as it uses built in call stack, otherwise you use a normal stack to do iterative DFS. BFS is your standard layer traversal using a queue
