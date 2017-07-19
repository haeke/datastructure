"""
    challenge: write a function to find the second largest element in a binary search tree
    the find_second_largest function has a time complexity of O(h) where h is the height of the tree and O(1) in space complexity.
    If the tree is balanced the time complexity is O(logn)
"""

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right
"""
the 'rightmost' element in the BST will is the largest, this function just checks to see if there is an element other than None in the right node then returns the value
"""
def find_largest(root_node):
    current = root_node
    #check to see if a node exists on the right
    while current:
        if not current.right:
            return current.value
        current = current.right
"""
    the second largest
        if we have a left subtree but not a right subtree then the current node is the largestnode. The second largest must be the in the largest element in the left subtree.
        if we have a right child but that right child node doesn't have any children then the right child must be the largest element and our current node must be the second largest
        if we have a right subtree with more than one element, the largest and second largest are in this tree
"""
def find_second_largest(root_node):
    if root_node is None or (root_node.left is None and root_node.fight is None):
        raise Exception('Tree must have at least two nodes')

    current = root_node

    while current:
        """
            current is the largest and has a left subtree
            the second largest is the largest in that subtree
        """
        if current.left and not current.right:
            return find_largest(current.left)
        """
            current is parent of largest and largest has no children
            so current is the 2nd largest
        """
        if current.right and not current.right.left and not current.right.right:
            return current.value

        current = current.right

secondlargest = BinaryTreeNode(4)

secondlargest.insert_left(3)
secondlargest.insert_right(5)

print find_largest(secondlargest)

print find_second_largest(secondlargest)
