'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false

 

Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100

 
Follow up: Could you solve it both recursively and iteratively?
'''
## Recursive solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        l = root.left
        r = root.right
        return self.recur_symmetry(l, r)
    
    def recur_symmetry(self, l, r):
        if (l == None and r != None) or (r == None and l != None):
            return False
        if l == None and r == None:
            return True
        if (l.val == r.val) and (l.left == None and l.right == None) and (r.left == None and r.right == None):
            return True
        elif (l.left == None and r.right != None) or (l.right == None and r.left != None):
            return False
        elif (l.left != None and r.right == None) or (l.right != None and r.left == None):
            return False
        if l.val == r.val:
            return self.recur_symmetry(l.left, r.right) and self.recur_symmetry(l.right, r.left)
        else:
            return False
        
## Iterative solution
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        elif root.left == None or root.right == None:
            return False
        q = deque()
        q.append(root.left)
        q.append(root.right)

        while q:
            l = q.popleft()
            r = q.popleft()

            if l is None and r is None:
                continue
            
            if l is None or r is None or l.val != r.val:
                return False
            
            q.append(l.left)
            q.append(r.right)
            q.append(l.right)
            q.append(r.left)

        return True