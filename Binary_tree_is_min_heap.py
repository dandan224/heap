 Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def isMinHeap(self, root):
    """
    input: TreeNode root
    return: boolean
    """
    # write your solution here
    if self.isCompleteBT(root) and self.isheapS(root):
      return True
    return False

  def isheapS(self, root):
    if not root:
      return True
    if not root.left and not root.right:
      return True
    if not root.right:
      return root.val <= root.left.val
    else:
      if root.left.val <= root.val and root.right.val <= root.val:
        return self.isheapS(root.left) and self.isheapS(root.right)
      return False   

  def isCompleteBT(self, root):
    if not root:
      return True
    queue = []
    # when a non ful node seen return True
    flag = False
    queue.append(root)
    while queue:
      node = queue.pop(0)
      if node.left:
        if flag == True:
          return False
        queue.append(node.left)
      else:
        flag = True
      if node.right:
        if flag == True:
          return False
        queue.append(node.right)
      else:
        flag = True
    return True
    
