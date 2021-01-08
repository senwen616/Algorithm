class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        result = []
        """
        def generate_trees(start,end):
            if start > end:
                return [None,]
            else:
                for i in range(start,end+1):
                    left_tree = generate_trees(start,i-1)
                    right_tree = generate_trees(i+1,end)
                    for l in left_tree:
                        for r in right_tree:
                            treeNode = TreeNode(i)
                            treeNode.left = l
                            treeNode.right = r
                            result.append(i)
                return result
        return generate_trees(1, n) if n else []
        """
        def generate_trees(start, end):
            if start > end:
                return [None, ]
            result = []
            for i in range(start, end + 1):
                left_tree = generate_trees(start, i - 1)
                right_tree = generate_trees(i + 1, end)
                for l in left_tree:
                    for r in right_tree:
                        treeNode = TreeNode(i)
                        treeNode.left = l
                        treeNode.right = r
                        result.append(treeNode)
            return result

        return generate_trees(1, n) if n else []