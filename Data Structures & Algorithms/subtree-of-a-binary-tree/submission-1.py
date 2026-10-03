class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: 
            return True # A null tree is always a subtree
        if not root: 
            return False # If root is null but subRoot isn't, it can't be a subtree
        
        # 1. Check if they are the exact same tree starting here
        if self.sameTree(root, subRoot): 
            return True
            
        # 2. Recursively search the left and right branches of the main tree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
        return False