#! coding: utf-8
class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right
root = TreeNode('A',TreeNode('B',TreeNode('D')),TreeNode('C',right=TreeNode('E')))
# 前序递归
# def preOrder(root):
#     if not root:
#         return None
#     print root.value
#     preOrder(root.left)
#     preOrder(root.right)
#
# preOrder(root)
#
# 前序非递归
def noRC(root):
    preorder = []
    if not root:
        return preOrder
    s = [root]
    while len(s) > 0:
        node = s.pop()
        preorder.append(node.value)
        if node.right:
            s.append(node.right)
        if node.left:
            s.append(node.left)
    return preorder
noRC(root)

def noRC(root):
    preorder = []
    if not root:
        return preorder
    s = [root]
    while s:
        node = s.pop()
        preorder.append(node.value)
        if node.right:
            s.append(node.right)
        if node.left:
            s.append(node.left)
    return preorder


class Solution:
    # def preorderTraversal(self, root: TreeNode) :
    #
    #     preorder = []
    #     if root is None:
    #         return preorder
    #
    #     s = [root]
    #     while len(s) > 0:
    #         node = s.pop()
    #         preorder.append(node.value)
    #         if node.right is not None:
    #             s.append(node.right)
    #         if node.left is not None:
    #             s.append(node.left)
    #
    #     return preorder

    def noRC(self,root):
        preorder = []
        if root is None:
            return preOrder
        s = [root]
        while len(s) > 0:
            node = s.pop()
            preorder.append(node.value)
            if node.right is not None:
                s.append(node.right)
            if node.left is not None:
                s.append(node.left)
        return preorder

if __name__ == '__main__':
    S = Solution()
    #print(S.preorderTraversal(root))
    print(S.noRC(root))