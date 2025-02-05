'''Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

Example 1:

Input: root = [1,null,2,3]

Output: [1,2,3]

Explanation:

Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [1,2,4,5,6,7,3,8,9]

Explanation:

Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]

 

Constraints:

    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

 

Follow up: Recursive solution is trivial, could you do it iteratively?
'''
#Iterative Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root == None:
            return res
        st = [root]
        while st:
            node = st.pop()
            res.append(node.val)

            if node.right != None:
                st.append(node.right)
            
            if node.left != None:
                st.append(node.left)
        return res
#Recursive Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root == None:
            return res
        return self.recurTraversal(root, res)

    def recurTraversal(self,root, res):
        if root == None:
            return res
        res.append(root.val)

        res = self.recurTraversal(root.left, res)
        res = self.recurTraversal(root.right, res)

        return res