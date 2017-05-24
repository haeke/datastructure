"""
    create  binary tree that implements a search() and print_tree()
    the tree is printed in pre-order traversal
"""

#initial setup for a node, setup an object with a value, left and
# right nodes are set to null initially

"""
    all other nodes will populate using left or right node parameter
    example -
    initial setup tree = BinaryTree(1)
    tree.root.left = Node(2)
"""
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

"""
    set the root of the tree, provide methods to traverse and print
"""

class BinaryTree(object):
    #constructor to set the root of the tree
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        return self.preorder_search(tree.root, find_val)

    def print_tree(self):
        """ print all tree nodes as they are visited in pre-order traversal """
        return self.preorder_print(self.root, "")

    def preorder_search(self, start, find_val):
        """ helper methods - recursive solution
        make sure start is an object, check if its the value we want
        if it is return true if not call the same function and search the left or right nodes until we find the correct value"""
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False

    def preorder_print(self, start, traversal):
        """ helprt method - recursive print """
        if start:
            traversal += (str(start.value) + ' ')
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

#test cases
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

#test searching  result expected is True
print tree.search(4)
#test search - result expected is False
print tree.search(7)

#test printing the tree
print tree.print_tree()
