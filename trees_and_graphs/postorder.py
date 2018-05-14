def rec_postorder(node, result):
  if node:
    rec_postorder(node.left, result)
    rec_postorder(node.right, result)
    result.append(node.val)

def iter_postorder(root):
  if not root:
    return

  result = []

  visited = set()
  stack = []
  node = root

  while stack or node:
    if node:
      stack.append(node)
      node = node.left
    else:
      node = stack.pop()

      if node.right and node.right not in visited:
        stack.append(node)
        node = node.right
      else:
        visited.add(node)
        result.append(node.val)
        node = None

  return result
