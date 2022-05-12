class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


# Create a class to initialize head and tail references
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def atBeg(self, value):
        new_node = Node( value )
        new_node.next = self.head
        self.head = new_node

    # def inMid(self, mid_node, value):
    #     if mid_node is None:
    #         print( "Mentioned node doesn't exist" )
    #         return
    #
    #     new_node = Node( value )
    #     new_node.next = mid_node.next
    #     mid_node.next = new_node

    def atEnd(self, value):
        new_node = Node( value )
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        self.tail = new_node

    def delBeg(self):
        if self.head is None:
            return
        elif self.head.next == self.tail.next:
            self.head = self.tail = None
            return
        elif self.head is not None:
            temp_node = self.head
            self.head = self.head.next
            temp_node = None
            return

    def delEnd(self):
        if self.head is None:
            return
        elif (self.head.next == self.tail.next):
            self.head = self.tail = None
            return
        else:
            temp_node = self.head
            while (temp_node.next is not self.tail):
                temp_node = temp_node.next
            self.tail = temp_node
            temp_node.next = None
        return

    def searchList(self, value):
        position = 0
        found = 0
        if self.head is None:
            print( "The linked list does not exist" )
        else:
            temp_node = self.head
            while temp_node is not None:
                position = position + 1
                if temp_node.value == value:
                    print( "The required value was found at position: " + str( position ) )
                    found = 1
                temp_node = temp_node.next
        if found == 0:
            print( "The required value does not exist in the list" )

    def printList(self):
        node_print = self.head
        while node_print is not None:
            print( node_print.value )
            node_print = node_print.next


singlyll = SinglyLinkedList()
temp_node1 = Node( 10 )
temp_node2 = Node( 20 )

singlyll.head = temp_node1
singlyll.head.next = temp_node2
singlyll.tail = temp_node2

singlyll.atBeg( 0 )
# mid=3
# singlyll.inMid(1,5)
singlyll.atEnd( 8 )

singlyll.printList()

print( singlyll.searchList( 7 ) )
