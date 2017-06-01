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

    The complexity of this algorithm is O(n)

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
