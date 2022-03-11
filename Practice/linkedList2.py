# create Node
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.prev = None
    
    # create a linkedList
    def insert(self, data):
        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(data)
        
        # 4. If the Linked List is empty, then make the
        #    new node as head
        # 5. Else traverse till the last node
        # 6. Change the next of last node
        if self.head == None:
            self.head = new_node
            self.prev = new_node
        else:
            self.prev.next = new_node
            self.prev = self.prev.next
    

    # Function to insert a new node at the beginning
    def push(self, new_data):
        # 1-2. Allocate the Node &
        # Put in the data
        new_node = Node(new_data)

        # 3. Make next of new Node as head
        new_node.next = self.head
        # 4. Move the head to point to new Node
        self.head = new_node


    # Inserts a new node after the given prev_node
    def insertAfter(self, prev_node, new_data):
        #1. check if the given prev_node exists
        if prev_node is None:
            print("The given previous data must be in linkedList")
            return
        
        # 2. Create new node &
        # 3. Put in the data
        new_node = Node(new_data)

        # 4. Make next of new Node as next of prev_node
        new_node.next = prev_node.next
        # 5. make next of prev_node as new_node
        prev_node.next = new_node
    


    # This function is defined in Linked List class
    # Appends a new node at the end.  This method is
    # defined inside LinkedList class shown above
    def append(self, new_data):

        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)

        # 4. If the Linked List is empty, then make the
        #    new node as head
        if self.head is None:
            self.head = new_node
            return

        # 5. Else traverse till the last node
        last = self.head
        while last.next:
            last = last.next

        # 6. Change the next of last node
        last.next = new_node

    # Given a reference to the head of a list and a key,
    # delete the first occurrence of key in linked list
    def deleteNode(self, key):

        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if temp == None:
            return

        # Unlink the node from linked list
        prev.next = temp.next
        temp = None


    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    
    # print the linked list
    def printLinkedList(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next