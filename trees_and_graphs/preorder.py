def rec_preorder(node, result):
  if node:
    result.append(node.val)
    rec_preorder(node.left, result)
    rec_preorder(node.right, result)

#Basically a DFS
def iter_preorder(root):
  if not root:
    return
  
  result = []

  stack = [root]

  while stack:
    node = stack.pop()

    result.append(node.val)

    if node.right:
      stack.append(node.right)
    if node.left:
      stack.append(node.left) #Done second so it gets popped off first

  return result
