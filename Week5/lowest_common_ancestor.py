##########################################
# Given a binary tree, find the lowest 
# common ancestor (LCA) of two given nodes 
# in the tree.
##########################################
def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    stack = [root]
    parent = {root: None}
    while p not in parent or q not in parent:

        node = stack.pop()
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)
    ancestors = set()
    while p:
        ancestors.add(p)
        p = parent[p]

    while q not in ancestors:
        q = parent[q]
    return q
