"""Given two strings s and t, determine whether some anagram of t is a
substring of s. For example: if s = "udacity" and t = "ad", then the
function returns True. Your function definition should look like:
question1(s, t) and return a boolean True or False."""

"""
    To solve this problem I would need to get the length of both the word we want to check and the word we want to check it with. Make sure that the word we are checking to be an anagram is smaller than the target word. Create the strings to lists, sort them and compare them to see if they contain the same letters.



"""

def is_anagram(s_1, s_2):
    """
        create lists of the two strings, so that we can sort them
        sort them, return comparison of each

        Time Complexity is O(n^2)
        Space Complexity is O(n)
    """
    s_1 = list(s_1)
    s_2 = list(s_2)
    print s_1
    s_1.sort()
    s_2.sort()
    return s_1 == s_2

#s contains the original, t contains the string we want to check
def question1(s, t):

    #get the lengh of both string we want to compare
    s_len = len(s)
    t_len = len(t)

    if(s_len < t_len):
        return False

    print s_len, t_len

    #set a range the length of the string we want to compare to
    for i in range(s_len - t_len + 1):
        #check for t in original string
        if is_anagram(s[i: i + t_len], t):
            return True
    return False


print(question1("udacity", "uda"))

print(question1("onetwothree", "three"))

print(question1("to", "tw"))


"""Given a string a, find the longest palindromic substring contained in a.
Your function definition should look like question2(a), and return a string."""

"""

    To check to see if each substring is a palindrome or not, we check all the substrings with ret_substrings one by one we need to fix the corner character until we loop through the word, then check it against the original word that we want to check for.

    Complexity is O(n^3)
    Space Complexity is O(n^2)

"""

def ret_substrings(s):
    l = len(s)

    for e in range(l, 0, -1):
        for i in range(l - e + 1):
            #return an object containing the substring from largest to shortest
            yield s[i: i+e]

# Define palindrome.
def palindrome(s):
    #check to see if the substring is the same as the string provided
    return s == s[::-1]

#for the string provided get all the substrings
#compare them to the string provided then return
def question2(a):
    for l in ret_substrings(a):
        if palindrome(l):
            return l

# Simple test case.
print question2("moms")


"""
Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this:
"""

"""
    I used kruskals algorithm to create the minimum spanning tree. This algorithm requires that I sort all the edges in non-decreasing order of their weight. after we pick the smallest edge we need to make sure that it does not form a cycle with the spanning tree formed so far, if it is not a cycle add the edge with a union, if it is then skip over it. This process will continue until n - 1 where n is the number of verticies.

    The time complexity is O(ElogE) where E are the number of edges
    The space complexity is O(n^2)

"""

#find a set that belongs to the parent
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

#create a union of two sets, x and y by rank if they are the same then make the root one
def union(parent, rank, x, y):
    rootx = find(parent, x)
    rooty = find(parent, y)

    if rank[rootx] < rank[rooty]:
        parent[rootx] = rooty
    elif rank[rootx] > rank[rooty]:
        parent[rooty] = rootx
    #handle same ranks
    else:
        parent[rooty] = rootx
        rank[rootx] += 1

def MST(graph, vertex, inv_dict):
    result = []

    i = 0
    e = 0

    #sort the graph provided in non-decreasing order
    graph = sorted(graph, key=lambda item: item[2])

    parent = []
    rank = []

    #create V subsets with single Nodes
    for node in range(vertex):
        parent.append(node)
        rank.append(0)

    n = vertex - 1

    while e < n:
        #pick the smallest edge and increment the index
        u,v,w = graph[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)

        #make sure edges aren't the same or a cycle will occur
        #add it to the result list and increment the index for the next edge
        if x != y:
            e += 1
            result.append([u,v,w])
            union(parent, rank, x, y)

    #print what is in result list - aka the MST
    p1 = []
    final_result = {}
    for u,v,weight in result:
        p1 = [(inv_dict[v], weight)]
        if inv_dict[u] not in final_result:
            final_result[inv_dict[u]] = p1
        else:
            final_result[inv_dict[u]] = final_result[inv_dict[u]].append(p1)

    return final_result

def question3(s1):

    tmp_dict = {}
    inv_dict = {}
    count = 0
    #store the nodeto, nodefrom and weight
    u,v,w = None, None, None
    graph = []

    for i in s1:
        tmp_dict[i] = count
        inv_dict[count] = i
        count += 1
   #iterate through the
    for i in s1:
        for j in s1[i]:
            u,v,w = tmp_dict[i], tmp_dict[j[0]], j[1]
            graph.append([u,v,w])

    return MST(graph, count, inv_dict)

s1 = {'A': [('B', 2)],
          'B': [('A', 4), ('C', 2)],
          'C': [('A', 2), ('B', 5)]}

print question3(s1)


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

    Time Complexity is O(n^3logn)
    Space Complexity is O(n^2)
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


"""
Find the element in a singly linked list that's m elements from the end.
For example, if a linked list has 5 elements, the 3rd element from the end is
the 3rd element. The function definition should look like question5(ll, m),
where ll is the first node of a linked list and m is the "mth number from the
end". You should copy/paste the Node class below to use as a representation of
a node in the linked list. Return the value of the node at that position.
e.g. 10->20->30->40->50
"""

"""
    One way to solve this problem is to create a linked list with two pointers to the head element. One will find the nth location in the linked list, by doing this we can check to see if the nth number is not larger than the linked list. Then we will go through both pointers until we go to the end, then return the other pointers data.

    The time complexity of this algorithm is O(n)
    The space complexity is O(n)

    One mention I would make about this method is that I need to use a global to keep track of the head variable that is shared between my methods because it is a bit easier to read. If I could change this again I would just create another class called linkedlist containing the head variable, adding an item to the linked list (push method) and the search for the nth element.
"""

global head
head = None

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

def push(data):
    global head
    new_node = Node(data)
    new_node.next = head
    head = new_node

def question5(head, n):
    #create two pointers, one to iterate through n list items
    #the other to get to the target we are looking for
    main_ptr = head
    reference_ptr = head
    count = 0

    #make sure the head isn't empty
    if(head != None):
        #iterate through the list until we get to n items
        while(count < n):
            #check to make sure we the nth node isn't larger than the linked list
            if(reference_ptr is None):
                print "%d is greater than the num of nodes" %(n)
                break
            #iterate through until we get to the end of the linked list
            reference_ptr = reference_ptr.next
            #increment count
            count += 1
        while(reference_ptr != None):
            main_ptr = main_ptr.next
            reference_ptr = ref_ptr.next

        return main_ptr.data

push(5)
push(6)
push(9)

print "The nth element is: %d" % question5(head, 3)
