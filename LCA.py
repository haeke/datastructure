"""

Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is the farthest node from the root that is an ancestor of both nodes. For example, the root is a common ancestor of all nodes on the tree, but if both nodes are descendents of the root's left child, then that left child might be the lowest common ancestor. You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. The function definition should look like question4(T, r, n1, n2), where T is the tree represented as a matrix, where the index of the list is equal to the integer stored in that node and a 1 represents a child node, r is a non-negative integer representing the root, and n1 and n2 are non-negative integers representing the two nodes in no particular order. For example, one test case might be

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
and the answer would be 3.

"""

"""
    To complete this question I needed to create a binary search tree out of the matrix that was provided. Then I placed nodes that were provided given the rules of a binary search tree ( cannot be larger than the root, anything smaller than the current head should move to the left, anything larger than the head should move to the right).
"""

class Node:

    # Constructor to create a new node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def children(self):
        return [self.left, self.right]

    def show(self):
        l = self.left.value if (self.left) else None
        r = self.right.value if (self.right) else None
        print "{} -> {}, {}".format(self.value, l, r)

# binary search tree
class binsearchtree(object):

    # init tree
    def __init__(self, root):
        self.root = Node(root)

    # insert new node in the tree
    def insert(self, new_val):
        self.insert_rule(self.root, new_val)

    # find the correct location for the new node in the tree
    # if the current value is less than insert right
    #if the current value is more than insert left
    def insert_rule(self, current, new_val):
        if current.value < new_val:
            if current.right:
                self.insert_rule(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self.insert_rule(current.left, new_val)
            else:
                current.left = Node(new_val)

    def show(self):
        self.root.show()
        children = self.root.children()
        while(len(children) > 0):
            child = children.pop(0)
            if child:
                child.show()
                children = children + child.children()

# build tree from the matrix T
def buildTree(tree, node):
    if T and node in T:
        children = T[node]
        for index, child in enumerate(children):
            if child == 1:
                tree.insert(index)
                buildTree(tree, index)

# find LCA of n1 and n2
def leastcommon(root, n1, n2):

    #the root cannot be empty
    if root is None:
        return None

    # if both n1 and n2 are smaller than root, then move left
    if(root.value > n1 and root.value > n2):
        return leastcommon(root.left, n1, n2)

    # if both n1 and n2 are greater than root, then move right
    if(root.value < n1 and root.value < n2):
        return leastcommon(root.right, n1, n2)

    return root


def question4(T, r, n1, n2):

    tree = binsearchtree(r)
    buildTree(tree, r)

    # find leastcommon
    return leastcommon(tree.root, n1, n2)


T = [[0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [1, 0, 0, 0, 1],
     [0, 0, 0, 0, 0]]
r = 3
n1 = 1
n2 = 4
test1 = question4(T, r, n1, n2) # expect 3
print "Test one should be 3: the number is %d" % test1.value

T = [[0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [1, 0, 0, 0, 1],
     [0, 0, 0, 0, 0]]
r = 5
n1 = 10
n2 = 10
test2 = question4(T, r, n1, n2) #expect none
print "Test two should be None: the number is %d" % test2.value
