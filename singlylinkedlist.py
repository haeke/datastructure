"""
    delete a node from a singly linked list given only a variable pointing to that node

    since we do not need to search the node for the node we want to delete we can just set the node to the node that proceeds it
    this will detach the node we don't want and python's garbage collector will take care of deleting the node.

    time complexity is O(1) and space complexity is O(1)

"""
def delete_node(delete_me):
    """
        we can take value and next from the input nodes next node and copy them into the input node.
        python's garbage collector will take care of deleting the node that we don't want anymore
    """
    #get the node that proceeds the node we want to delete
    next_node = delete_me.next

    if next_node:
        #set the value of delete_me to the value in next_node
        delete_me.value = next_node.value
        #set the pointer of delete_me to the pointer in next_node
        delete_me.next = next_node.next
        print "New value is %s" % next_node.value
    else:
        """
            we are trying to delete the last node
        """
        raise Exception("cannot delete the last node with this method")

class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next = None

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c

delete_node(b)
"""
    since we are provided with the node that we want to delete we can change the previous nodes pointer to skip the node we want to delete,
    this will make the previous node point to the node that is after the node b in this example which is node c.
""" 
