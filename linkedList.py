"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            #set next for the end of the list to be the new element
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        counter = 1
        #set the current position to be the head
        current = self.head
        #if the position does not start at one return nothing
        if position < 1:
            return None
        while current and counter <= position:
            #if the current counter is the position we found it
            if counter == position:
                return current
            #create a pointer to go to the next item in the linked list
            current = current.next
            #increment the counter to check the next location
            counter += 1
        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        #handle the case where we insert after the first item in the link list
        elif position == 1:
            new_element.next = self.head
            self.head = new_element


    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        #check if the current value is the value passed and that theres another element that proceeds it
        while current.value != value and current.next:
            #set the current value to previous
            previous = current
            #set the next item to be the current item
            current = current.next
        if current.value == value:
            if previous:
                #set the next pointer to the element after the element we want to delete so we don't lose it
                previous.next = current.next
            else:
                self.head = current.next

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4,3)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value
