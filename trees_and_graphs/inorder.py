def rec_inorder(node, result):
  if node:
    rec_inorder(node.left, result)
    result.append(node.val)
    rec_inorder(node.right, result)

def iter_inorder(root):
  if not root:
    return

  result = []

  stack = []
  node = root

  while stack or node:
    if node:
      stack.append(node)
      node = node.left
    else:
      node = stack.pop()
      result.append(node.val)
      node = node.right
  
  return result
