"""
    ***always keep a pointer to the root node to access the first node in the list


"""

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

class LinkedList:
    #construct to initialize head
    def __init__(self):
        self.head = None

    #function to insert a new node at the beginning
    def push(self, new_data):
        new_node = LinkedListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    #delete the head of a list and a position
    def delete_node(self, position):
        #if the list is empty
        if self.head == None:
            return

        #temp head node
        temp = self.head

        #if head needs to be removed
        if position == 0:
            self.head = temp.next
            temp = None
            return

        #find previous node of the node to be deleted
        for i in range(position - 1):
            temp = temp.next
            if temp == None:
                break

        #if position is more than the number of nodes
        if temp == None:
            return
        if temp.next == None:
            return

        #node temp.next is teh node to be deleted
        #store pointer to the next of the node to be deleted
        next = temp.next.next

        #unlink the node from the linked list
        temp.next = None

        temp.next = next

    #print the linked list
    def printList(self):
        temp = self.head
        while(temp):
            print " %d " %(temp.value),
            temp = temp.next

linkedlist = LinkedList()

linkedlist.push(1)
linkedlist.push(2)
linkedlist.push(3)

#print the list
linkedlist.printList()
