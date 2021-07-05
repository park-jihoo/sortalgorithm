class traversal:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        result = []
        def help(node):
            if node is None:
                return
            help(node.left)
            result.append(node.val)
            help(node.right)
        help(root)
        return result
