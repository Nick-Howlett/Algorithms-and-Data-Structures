class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
      return self.array_to_trees([i for i in range(1, n + 1)])
    
    
    def array_to_trees(self, arr):
      if len(arr) == 1:
        return [TreeNode(arr[0])]
      ret = []
      for i in range(len(arr)):
        left_possibilities = self.array_to_trees(arr[:i])
        right_possibilities = self.array_to_trees(arr[i + 1:])
        for lpos in left_possibilities:
          for rpos in right_possibilities:
            root = TreeNode(arr[i])
            root.left = lpos
            root.right = rpos
            ret.append(root)
        if not left_possibilities:
          for pos in right_possibilities:
            root = TreeNode(arr[i])
            root.right = pos
            ret.append(root)
        if not right_possibilities:
          for pos in left_possibilities:
            root = TreeNode(arr[i])
            root.left = pos
            ret.append(root)
      return ret