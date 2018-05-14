#Recursive tree traversals
def rec_preorder(node, result):
  if node:
    result.append(node.val)
    rec_preorder(node.left, result)
    rec_preorder(node.right, result)

def rec_inorder(node, result):
  if node:
    rec_inorder(node.left, result)
    result.append(node.val)
    rec_inorder(node.right, result)

def rec_postorder(node, result):
  if node:
    rec_postorder(node.left, result)
    rec_postorder(node.right, result)
    result.append(node.val)

#Iterative tree traversals

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

#Iterative Binary Search Tree Inorder traversals

def iterative_BST_Inorder_traversal1(root):
  stack = []
  current = root

  while True:
      if current:
          stack.append(current)
          current = current.left
      else:
          if stack:
              node = stack.pop()
              print(node.val)
              current = node.right
          else:
              break

def iterative_BST_Inorder_traversal2(root):
  stack = []

  while root or stack:
      while root:
          stack.append(root)
          root = root.left
      
      root = stack.pop()
      print(root.val) #******
      root = root.right

'''
#**** part can be used for 
A. Kth smallest element in a BST, 
     just --k and check for it to hit 0 -> break and return root val
B. Validate binary search tree (doesn't work nicely for dupe values since
you have to account for dupes being on right or left side)
'''

'''
Misc
* Inorder traversal for a Binary Search Tree gives sorted list

'''

class Node:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

def main():
  #Build test tree
  #      0
  #    /   \
  #   1     2
  #  / \   /  \
  # 3   4 5    6
  root = Node(0)
  root.left, root.right  = Node(1), Node(2)
  root.left.left, root.left.right = Node(3), Node(4)
  root.right.left, root.right.right = Node(5), Node(6)


  print('Preorder:  0 1 3 4 2 5 6')
  res = []
  rec_preorder(root, res)
  pprint(res)
  res = iter_preorder(root)
  pprint(res)
  print()

  print('Inorder:   3 1 4 0 5 2 6')
  res = []
  rec_inorder(root, res)
  pprint(res)
  res = iter_inorder(root)
  pprint(res)
  print()

  print('Postorder: 3 4 1 5 6 2 0')
  res = []
  rec_postorder(root, res)
  pprint(res)
  res = iter_postorder(root)
  pprint(res)
  print()



def pprint(l):
  print('           ' + ' '.join([str(x) for x in l]))


if __name__ == '__main__':
  main()
