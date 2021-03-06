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

from preorder import *
from inorder import *
from postorder import *
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
